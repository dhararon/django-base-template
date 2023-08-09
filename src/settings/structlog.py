import structlog

LOG_RECORD_ATTRIBUTES = {
    "args",
    "asctime",
    "created",
    "exc_info",
    "exc_text",
    "filename",
    "funcName",
    "levelname",
    "levelno",
    "lineno",
    "message",
    "module",
    "msecs",
    "msg",
    "name",
    "pathname",
    "process",
    "processName",
    "relativeCreated",
    "stack_info",
    "thread",
    "threadName",
}
BASIC_TYPES = (str, bool, int, float, type(None))


def structlog_to_stdlib_adapter(logger, method_name, event_dict):  # noqa:ARG001
    """Pass the `event_dict` as `extra` keyword argument to the standard logger."""
    exclude_keys = ["logger", "level"]
    event = event_dict.pop("event", "")
    for key in exclude_keys:
        event_dict.pop(key, None)
    # Rename keys that conflict with the reserved LogRecord attributes
    conflicting_keys = set(event_dict) & LOG_RECORD_ATTRIBUTES
    for key in conflicting_keys:
        event_dict[key + "_"] = event_dict.pop(key)
    # Replace extra values of non-basic types with their string representation to make
    # sure they will become JSON-serializable (essential for logstash logging handler).
    event_dict = {k: v if isinstance(v, BASIC_TYPES) else repr(v) for k, v in event_dict.items()}
    kwargs = {
        "extra": event_dict,
        "exc_info": "exception" in event_dict,
    }
    return (event,), kwargs


def extract_stdlib_extra(logger, method_name, event_dict):  # noqa:ARG001
    """
    Extract the `extra` key-values from the standard logger record
    and populate the `event_dict` with them.
    """
    record_extra = {k: v for k, v in vars(event_dict["_record"]).items() if k not in LOG_RECORD_ATTRIBUTES}
    event_dict.update(record_extra)
    return event_dict


class BaseStructlog:
    @classmethod
    def _configure_logs(cls):
        structlog.configure(
            processors=[
                structlog.stdlib.filter_by_level,
                structlog.stdlib.add_logger_name,
                structlog.stdlib.add_log_level,
                structlog.stdlib.PositionalArgumentsFormatter(),
                structlog.processors.TimeStamper(fmt="%Y-%m-%d %H:%M:%S"),
                structlog.processors.StackInfoRenderer(),
                structlog.processors.format_exc_info,
                structlog.processors.UnicodeDecoder(),
                structlog_to_stdlib_adapter,
            ],
            logger_factory=structlog.stdlib.LoggerFactory(),
            wrapper_class=structlog.stdlib.BoundLogger,
            cache_logger_on_first_use=True,
        )

    @property
    def LOGGING(self):  # noqa: N802
        return {
            "version": 1,
            "disable_existing_loggers": False,
            "loggers": {
                "django_structlog": {
                    "handlers": [
                        "console",
                    ],
                    "level": "INFO",
                }
            },
            "formatters": {
                "colored": {
                    "()": structlog.stdlib.ProcessorFormatter,
                    "processor": structlog.dev.ConsoleRenderer(colors=True),
                    "foreign_pre_chain": [
                        # Add logger name, log level, timestamp and extra dict to
                        # the event_dict if the log entry is not from structlog.
                        structlog.stdlib.add_logger_name,
                        structlog.stdlib.add_log_level,
                        structlog.processors.TimeStamper(fmt="%Y-%m-%d %H:%M:%S"),
                        structlog.processors.format_exc_info,
                        extract_stdlib_extra,
                    ],
                },
            },
            "handlers": {
                "console": {
                    "level": "DEBUG",
                    "class": "logging.StreamHandler",
                    "formatter": "colored",
                },
            },
        }

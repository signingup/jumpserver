# -*- coding: utf-8 -*-
#
from ..const import CONFIG

# Storage settings
COMMAND_STORAGE = {
    'ENGINE': 'terminal.backends.command.db',
}
DEFAULT_TERMINAL_COMMAND_STORAGE = {
    "default": {
        "TYPE": "server",
    },
}
TERMINAL_COMMAND_STORAGE = CONFIG.TERMINAL_COMMAND_STORAGE or {}

# Server 类型的录像存储
SERVER_REPLAY_STORAGE = CONFIG.SERVER_REPLAY_STORAGE
# SERVER_REPLAY_STORAGE = {
#     'TYPE': 's3',
#     'BUCKET': '',
#     'ACCESS_KEY': '',
#     'SECRET_KEY': '',
#     'ENDPOINT': ''
# }

DEFAULT_TERMINAL_REPLAY_STORAGE = {
    "default": {
        "TYPE": "server",
    },
}
TERMINAL_REPLAY_STORAGE = CONFIG.TERMINAL_REPLAY_STORAGE

# Security settings
SECURITY_MFA_AUTH = CONFIG.SECURITY_MFA_AUTH
SECURITY_COMMAND_EXECUTION = CONFIG.SECURITY_COMMAND_EXECUTION
SECURITY_LOGIN_LIMIT_COUNT = CONFIG.SECURITY_LOGIN_LIMIT_COUNT
SECURITY_LOGIN_LIMIT_TIME = CONFIG.SECURITY_LOGIN_LIMIT_TIME  # Unit: minute
SECURITY_MAX_IDLE_TIME = CONFIG.SECURITY_MAX_IDLE_TIME  # Unit: minute
SECURITY_PASSWORD_EXPIRATION_TIME = CONFIG.SECURITY_PASSWORD_EXPIRATION_TIME # Unit: day
SECURITY_PASSWORD_MIN_LENGTH = CONFIG.SECURITY_PASSWORD_MIN_LENGTH  # Unit: bit
SECURITY_ADMIN_USER_PASSWORD_MIN_LENGTH = CONFIG.SECURITY_ADMIN_USER_PASSWORD_MIN_LENGTH  # Unit: bit
OLD_PASSWORD_HISTORY_LIMIT_COUNT = CONFIG.OLD_PASSWORD_HISTORY_LIMIT_COUNT
SECURITY_PASSWORD_UPPER_CASE = CONFIG.SECURITY_PASSWORD_UPPER_CASE
SECURITY_PASSWORD_LOWER_CASE = CONFIG.SECURITY_PASSWORD_LOWER_CASE
SECURITY_PASSWORD_NUMBER = CONFIG.SECURITY_PASSWORD_NUMBER
SECURITY_PASSWORD_SPECIAL_CHAR = CONFIG.SECURITY_PASSWORD_SPECIAL_CHAR
SECURITY_PASSWORD_RULES = [
    'SECURITY_PASSWORD_MIN_LENGTH',
    'SECURITY_PASSWORD_UPPER_CASE',
    'SECURITY_PASSWORD_LOWER_CASE',
    'SECURITY_PASSWORD_NUMBER',
    'SECURITY_PASSWORD_SPECIAL_CHAR'
]
SECURITY_MFA_VERIFY_TTL = CONFIG.SECURITY_MFA_VERIFY_TTL
SECURITY_VIEW_AUTH_NEED_MFA = CONFIG.SECURITY_VIEW_AUTH_NEED_MFA
SECURITY_SERVICE_ACCOUNT_REGISTRATION = CONFIG.SECURITY_SERVICE_ACCOUNT_REGISTRATION
SECURITY_LOGIN_CAPTCHA_ENABLED = CONFIG.SECURITY_LOGIN_CAPTCHA_ENABLED
SECURITY_LOGIN_CHALLENGE_ENABLED = CONFIG.SECURITY_LOGIN_CHALLENGE_ENABLED
SECURITY_DATA_CRYPTO_ALGO = CONFIG.SECURITY_DATA_CRYPTO_ALGO
SECURITY_INSECURE_COMMAND = CONFIG.SECURITY_INSECURE_COMMAND
SECURITY_INSECURE_COMMAND_LEVEL = CONFIG.SECURITY_INSECURE_COMMAND_LEVEL
SECURITY_INSECURE_COMMAND_EMAIL_RECEIVER = CONFIG.SECURITY_INSECURE_COMMAND_EMAIL_RECEIVER

# Terminal other setting
TERMINAL_PASSWORD_AUTH = CONFIG.TERMINAL_PASSWORD_AUTH
TERMINAL_PUBLIC_KEY_AUTH = CONFIG.TERMINAL_PUBLIC_KEY_AUTH
TERMINAL_HEARTBEAT_INTERVAL = CONFIG.TERMINAL_HEARTBEAT_INTERVAL
TERMINAL_ASSET_LIST_SORT_BY = CONFIG.TERMINAL_ASSET_LIST_SORT_BY
TERMINAL_ASSET_LIST_PAGE_SIZE = CONFIG.TERMINAL_ASSET_LIST_PAGE_SIZE
TERMINAL_SESSION_KEEP_DURATION = CONFIG.TERMINAL_SESSION_KEEP_DURATION
TERMINAL_HOST_KEY = CONFIG.TERMINAL_HOST_KEY
TERMINAL_HEADER_TITLE = CONFIG.TERMINAL_HEADER_TITLE
TERMINAL_TELNET_REGEX = CONFIG.TERMINAL_TELNET_REGEX

# Asset user auth external backend, default AuthBook backend
BACKEND_ASSET_USER_AUTH_VAULT = False

PERM_SINGLE_ASSET_TO_UNGROUP_NODE = CONFIG.PERM_SINGLE_ASSET_TO_UNGROUP_NODE
PERM_EXPIRED_CHECK_PERIODIC = CONFIG.PERM_EXPIRED_CHECK_PERIODIC
WINDOWS_SSH_DEFAULT_SHELL = CONFIG.WINDOWS_SSH_DEFAULT_SHELL
FLOWER_URL = CONFIG.FLOWER_URL

# Enable internal period task
PERIOD_TASK_ENABLED = CONFIG.PERIOD_TASK_ENABLED

# only allow single machine login with the same account
USER_LOGIN_SINGLE_MACHINE_ENABLED = CONFIG.USER_LOGIN_SINGLE_MACHINE_ENABLED

# Email custom content
EMAIL_SUBJECT_PREFIX = CONFIG.EMAIL_SUBJECT_PREFIX
EMAIL_SUFFIX = CONFIG.EMAIL_SUFFIX
EMAIL_CUSTOM_USER_CREATED_SUBJECT = CONFIG.EMAIL_CUSTOM_USER_CREATED_SUBJECT
EMAIL_CUSTOM_USER_CREATED_HONORIFIC = CONFIG.EMAIL_CUSTOM_USER_CREATED_HONORIFIC
EMAIL_CUSTOM_USER_CREATED_BODY = CONFIG.EMAIL_CUSTOM_USER_CREATED_BODY
EMAIL_CUSTOM_USER_CREATED_SIGNATURE = CONFIG.EMAIL_CUSTOM_USER_CREATED_SIGNATURE

DISPLAY_PER_PAGE = CONFIG.DISPLAY_PER_PAGE
DEFAULT_EXPIRED_YEARS = 70
USER_GUIDE_URL = CONFIG.USER_GUIDE_URL
HTTP_LISTEN_PORT = CONFIG.HTTP_LISTEN_PORT
WS_LISTEN_PORT = CONFIG.WS_LISTEN_PORT
LOGIN_LOG_KEEP_DAYS = CONFIG.LOGIN_LOG_KEEP_DAYS
TASK_LOG_KEEP_DAYS = CONFIG.TASK_LOG_KEEP_DAYS
ORG_CHANGE_TO_URL = CONFIG.ORG_CHANGE_TO_URL
WINDOWS_SKIP_ALL_MANUAL_PASSWORD = CONFIG.WINDOWS_SKIP_ALL_MANUAL_PASSWORD

AUTH_EXPIRED_SECONDS = 60 * 5

CHANGE_AUTH_PLAN_SECURE_MODE_ENABLED = CONFIG.CHANGE_AUTH_PLAN_SECURE_MODE_ENABLED

DATETIME_DISPLAY_FORMAT = '%Y-%m-%d %H:%M:%S'

TICKETS_ENABLED = CONFIG.TICKETS_ENABLED
REFERER_CHECK_ENABLED = CONFIG.REFERER_CHECK_ENABLED

CONNECTION_TOKEN_ENABLED = CONFIG.CONNECTION_TOKEN_ENABLED
FORGOT_PASSWORD_URL = CONFIG.FORGOT_PASSWORD_URL


# 自定义默认组织名
GLOBAL_ORG_DISPLAY_NAME = CONFIG.GLOBAL_ORG_DISPLAY_NAME
HEALTH_CHECK_TOKEN = CONFIG.HEALTH_CHECK_TOKEN

TERMINAL_RDP_ADDR = CONFIG.TERMINAL_RDP_ADDR
SECURITY_LUNA_REMEMBER_AUTH = CONFIG.SECURITY_LUNA_REMEMBER_AUTH
SECURITY_WATERMARK_ENABLED = CONFIG.SECURITY_WATERMARK_ENABLED
SECURITY_SESSION_SHARE = CONFIG.SECURITY_SESSION_SHARE

LOGIN_REDIRECT_TO_BACKEND = CONFIG.LOGIN_REDIRECT_TO_BACKEND
LOGIN_REDIRECT_MSG_ENABLED = CONFIG.LOGIN_REDIRECT_MSG_ENABLED

CLOUD_SYNC_TASK_EXECUTION_KEEP_DAYS = CONFIG.CLOUD_SYNC_TASK_EXECUTION_KEEP_DAYS

import os

from rasa.shared.constants import DOCS_BASE_URL

DEFAULT_ENDPOINTS_PATH = "endpoints.yml"
DEFAULT_CREDENTIALS_PATH = "credentials.yml"
DEFAULT_CONFIG_PATH = "config.yml"
DEFAULT_DOMAIN_PATH = "domain.yml"
DEFAULT_ACTIONS_PATH = "actions"
DEFAULT_MODELS_PATH = "models"
DEFAULT_CONVERTED_DATA_PATH = "converted_data"
DEFAULT_DATA_PATH = "data"
DEFAULT_RESULTS_PATH = "results"
DEFAULT_NLU_RESULTS_PATH = "nlu_comparison_results"
DEFAULT_CORE_SUBDIRECTORY_NAME = "core"
DEFAULT_NLU_SUBDIRECTORY_NAME = "nlu"
DEFAULT_REQUEST_TIMEOUT = 60 * 5  # 5 minutes
DEFAULT_RESPONSE_TIMEOUT = 60 * 60  # 1 hour

TEST_DATA_FILE = "test.md"
TRAIN_DATA_FILE = "train.md"
NLG_DATA_FILE = "responses.md"
RESULTS_FILE = "results.json"
NUMBER_OF_TRAINING_STORIES_FILE = "num_stories.json"
PERCENTAGE_KEY = "__percentage__"

PACKAGE_NAME = "rasa"

DEFAULT_RASA_X_PORT = 5002
DEFAULT_RASA_PORT = 5005

DOCS_URL_POLICIES = DOCS_BASE_URL + "/policies"
DOCS_URL_TEST_STORIES = DOCS_BASE_URL + "/testing-your-assistant"
DOCS_URL_ACTIONS = DOCS_BASE_URL + "/actions"
DOCS_URL_CONNECTORS = DOCS_BASE_URL + "/connectors/"
DOCS_URL_EVENT_BROKERS = DOCS_BASE_URL + "/event-brokers"
DOCS_URL_PIKA_EVENT_BROKER = DOCS_URL_EVENT_BROKERS + "#pika-event-broker"
DOCS_URL_TRACKER_STORES = DOCS_BASE_URL + "/tracker-stores"
DOCS_URL_PIPELINE = DOCS_BASE_URL + "/tuning-your-model"
DOCS_URL_COMPONENTS = DOCS_BASE_URL + "/components"
DOCS_URL_MIGRATION_GUIDE = DOCS_BASE_URL + "/migrate-from/"

DOCS_BASE_URL_RASA_X = "https://rasa.com/docs/rasa-x"

CONFIG_KEYS_CORE = ["policies"]
CONFIG_KEYS_NLU = ["language", "pipeline"]
CONFIG_KEYS = CONFIG_KEYS_CORE + CONFIG_KEYS_NLU
CONFIG_MANDATORY_KEYS_CORE = []
CONFIG_MANDATORY_KEYS_NLU = ["language"]
CONFIG_MANDATORY_KEYS = CONFIG_MANDATORY_KEYS_CORE + CONFIG_MANDATORY_KEYS_NLU
CONFIG_AUTOCONFIGURABLE_KEYS_CORE = ["policies"]
CONFIG_AUTOCONFIGURABLE_KEYS_NLU = ["pipeline"]
CONFIG_AUTOCONFIGURABLE_KEYS = (
    CONFIG_AUTOCONFIGURABLE_KEYS_CORE + CONFIG_AUTOCONFIGURABLE_KEYS_NLU
)

MINIMUM_COMPATIBLE_VERSION = "2.0.0a3"

NEXT_MAJOR_VERSION_FOR_DEPRECATIONS = "3.0.0"

GLOBAL_USER_CONFIG_PATH = os.path.expanduser("~/.config/rasa/global.yml")

DEFAULT_LOG_LEVEL_RASA_X = "WARNING"
DEFAULT_LOG_LEVEL_LIBRARIES = "ERROR"
ENV_LOG_LEVEL_LIBRARIES = "LOG_LEVEL_LIBRARIES"

DEFAULT_SANIC_WORKERS = 1
ENV_SANIC_WORKERS = "SANIC_WORKERS"
ENV_SANIC_BACKLOG = "SANIC_BACKLOG"

DEFAULT_SESSION_EXPIRATION_TIME_IN_MINUTES = 0
DEFAULT_CARRY_OVER_SLOTS_TO_NEW_SESSION = True

ENV_GPU_CONFIG = "TF_GPU_MEMORY_ALLOC"
ENV_CPU_INTER_OP_CONFIG = "TF_INTER_OP_PARALLELISM_THREADS"
ENV_CPU_INTRA_OP_CONFIG = "TF_INTRA_OP_PARALLELISM_THREADS"

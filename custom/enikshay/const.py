# Case property names used in integrations
PRIMARY_PHONE_NUMBER = 'phone_number'
BACKUP_PHONE_NUMBER = 'secondary_contact_phone_number'
OTHER_NUMBER = "phone_number_other"
NINETYNINEDOTS_NUMBERS = [
    PRIMARY_PHONE_NUMBER,
    BACKUP_PHONE_NUMBER,
    OTHER_NUMBER,
]

MERM_ID = 'merm_id'
MERM_DAILY_REMINDER_STATUS = 'merm_daily_reminder_status'
MERM_DAILY_REMINDER_TIME = "merm_daily_reminder_time"
MERM_REFILL_REMINDER_STATUS = "merm_refill_reminder_status"
MERM_REFILL_REMINDER_DATETIME = "merm_refill_reminder_datetime"
MERM_RT_HOURS = "merm_rt_hours"
MERM_PROPERTIES = [
    MERM_ID,
    MERM_DAILY_REMINDER_STATUS,
    MERM_DAILY_REMINDER_TIME,
    MERM_REFILL_REMINDER_STATUS,
    MERM_REFILL_REMINDER_DATETIME,
    MERM_RT_HOURS,
]

ENROLLED_IN_PRIVATE = "enrolled_in_private"

ENIKSHAY_ID = 'person_id'
PERSON_FIRST_NAME = 'first_name'
PERSON_LAST_NAME = 'last_name'

TREATMENT_START_DATE = 'treatment_initiation_date'
TREATMENT_SUPPORTER_FIRST_NAME = 'treatment_supporter_first_name'
TREATMENT_SUPPORTER_LAST_NAME = 'treatment_supporter_last_name'
TREATMENT_SUPPORTER_PHONE = 'treatment_supporter_mobile_number'

TREATMENT_OUTCOME = 'treatment_outcome'
TREATMENT_OUTCOME_DATE = 'treatment_outcome_date'
EPISODE_PENDING_REGISTRATION = "episode_pending_registration"
WEIGHT_BAND = 'weight_band'
LAST_VOUCHER_CREATED_BY_ID = "bets_last_voucher_created_by_id"
NOTIFYING_PROVIDER_USER_ID = "bets_notifying_provider_user_id"

CURRENT_ADDRESS = 'current_address'
ENROLLED_IN_PRIVATE = "enrolled_in_private"

NINETYNINEDOTS_PERSON_PROPERTIES = [
    ENIKSHAY_ID,
    PRIMARY_PHONE_NUMBER,
    BACKUP_PHONE_NUMBER,
    OTHER_NUMBER,
    PERSON_FIRST_NAME,
    PERSON_LAST_NAME,
    CURRENT_ADDRESS,
    ENROLLED_IN_PRIVATE,
    'owner_id',
]
NINETYNINEDOTS_EPISODE_PROPERTIES = [
    TREATMENT_SUPPORTER_FIRST_NAME,
    TREATMENT_SUPPORTER_LAST_NAME,
    TREATMENT_SUPPORTER_PHONE,
    TREATMENT_OUTCOME,
    TREATMENT_OUTCOME_DATE,
    TREATMENT_START_DATE,
    WEIGHT_BAND,
] + MERM_PROPERTIES

DOSE_TAKEN_INDICATORS = [
    'directly_observed_dose',
    'unobserved_dose',
    'self_administered_dose',
]

DOSE_MISSED = 'missed_dose'
DOSE_UNKNOWN = 'missing_data'
DOSE_KNOWN_INDICATORS = DOSE_TAKEN_INDICATORS + [DOSE_MISSED]
DAILY_SCHEDULE_FIXTURE_NAME = 'adherence_schedules'
DAILY_SCHEDULE_ID = 'schedule_daily'
SCHEDULE_ID_FIXTURE = 'id'
# one of values of 'adherence_closure_reason' case property
HISTORICAL_CLOSURE_REASON = 'historical'
PRESCRIPTION_TOTAL_DAYS_THRESHOLD = "prescription_total_days_threshold_{}"

# Voucher Case Properties
DATE_FULFILLED = "date_fulfilled"
VOUCHER_ID = "voucher_id"
FULFILLED_BY_ID = "fulfilled_by_id"
AMOUNT_APPROVED = "amount_approved"

ENIKSHAY_TIMEZONE = 'Asia/Kolkata'

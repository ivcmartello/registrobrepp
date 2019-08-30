from enum import Enum


class RenewalType(Enum):
    LEGACY = 'legacy'
    MEMBER = 'member'
    END_USER = 'end-user'
    MICRO = 'micro'
    SMALL = 'small'
    MEDIUM = 'medium'
    LARGE = 'large'
    EXTRA_LARGE = 'extra-large'
    EXTRA_LARGE_LARGE = 'extra-large-large'
    FOUNDING_PARTNER = 'founding-partner'
    B_ACTIVE = 'b-active'

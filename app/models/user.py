from typing import Optional
from pydantic import BaseModel, Field

class UserStatsData(BaseModel):
    """A model for user stats for a specific mode."""

    total_score: int
    ranked_score: int
    pp: float
    play_count: int
    play_time: int
    accouracy: float = Field(..., le= 100)
    max_combo: int
    rank: int

class ModeStatsData(BaseModel):
    """Model of stats for all c_modes."""

    vn: list[UserStatsData]
    rx: list[UserStatsData]
    ap: list[UserStatsData]

class SmallClanData(BaseModel):
    """Model for basic clan data."""

    id: int
    tag: str
    name: str

class PlayerBadgeData(BaseModel):
    """Represents a singular badge."""

    id: int
    name: str
    icon: str

class PlayerCardData(BaseModel):
    """A model for player card data."""

    id: int
    name: str
    privileges: int
    stats: ModeStatsData
    clan: Optional[SmallClanData]
    badges: list[PlayerBadgeData]
    background_url: str

class UserCommentData(BaseModel):
    """Data for a user comment."""

    user: PlayerCardData
    content: str
    time: int
    hidden: bool

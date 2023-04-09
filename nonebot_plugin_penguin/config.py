from typing import Literal

from nonebot import get_driver
from pydantic import Field, BaseSettings


class PlugConfig(BaseSettings):
    penguin_mirrior: Literal["io", "cn"] = "io"
    penguin_show_count: int = 5

    # 以下配置项会自动生成，无需手动配置
    penguin_site: str = Field(default_factory=str)
    penguin_cdn: str = Field(default_factory=str)
    penguin_widget: str = Field(default_factory=str)

    # penguin_database: str = ""
    class Config:
        extra = "ignore"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        match self.penguin_mirrior:
            case "io":
                self.penguin_site: str = "https://penguin-stats.io"
                self.penguin_cdn: str = "https://penguin-stats.s3.amazonaws.com"
                self.penguin_widget: str = "https://widget.penguin-stats.io"
            case "cn":
                self.penguin_site: str = "https://penguin-stats.cn"
                self.penguin_cdn: str = "https://penguin.upyun.galvincdn.com"
                self.penguin_widget: str = "https://widget.penguin-stats.cn"
        # if self.penguin_database:
        #     self.penguin_database_path: Path = Path(self.penguin_database)
        # else:
        #     data_path: Path = Path.cwd() / "data"
        #     self.penguin_database_path: Path = data_path / "penguin.db"
        #     data_path.mkdir(exist_ok=True)


global_config = get_driver().config
plugin_config = PlugConfig(**global_config.dict())

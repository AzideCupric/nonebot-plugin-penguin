from pydantic import BaseModel

from .types import T_Lang, T_Query, T_Server, T_Sorted_Key, T_Filter_Mode


class Item(BaseModel):
    itemId: str
    name_i18n: dict[str, str]
    spriteCoord: list[int]


class Stage(BaseModel):
    stageId: str
    zoneId: str
    code_i18n: dict[str, str]
    apCost: int
    minClearTime: int


class Zone(BaseModel):
    zoneId: str
    zoneName_i18n: dict[str, str]
    type: str


class Matrix(BaseModel):
    stage: Stage
    zone: Zone
    item: Item
    percentage: float
    apPPR: float
    quantity: int
    times: int
    start: int
    end: int | None

    def export(self, mode: T_Query, lang: T_Lang):
        match mode:
            case "item":
                return RenderByItem(
                    stage_name=self.stage.code_i18n[lang],
                    zone=self.zone.zoneName_i18n[lang],
                    percent=str(self.percentage) + "%",
                    ap_ppr=str(self.apPPR),
                    rop_count=str(self.quantity),
                    simple_count=str(self.times),
                    open=True if self.end else False,
                )
            case "stage" | "exact":
                return RenderByStage(
                    item_name=self.item.name_i18n[lang],
                    sprite_coord=self.item.spriteCoord,
                    percent=str(self.percentage) + "%",
                    ap_ppr=str(self.apPPR),
                    rop_count=str(self.quantity),
                    simple_count=str(self.times),
                )


class Request(BaseModel):
    name: str  # 关卡或者掉落物名，两者都有时，关卡在前，空格隔开
    server: T_Server = "cn"
    type: T_Query
    ids: tuple[str, str] | tuple[str]
    lang: T_Lang = "zh"
    sort_by: T_Sorted_Key = "percentage"
    filter_by: T_Filter_Mode = "only_open"
    ignore_threshold: int = 100
    reverse: bool = False


class RenderByItem(BaseModel):
    stage_name: str
    zone: str
    percent: str
    ap_ppr: str
    rop_count: str
    simple_count: str
    open: bool


class RenderByStage(BaseModel):
    item_name: str
    sprite_coord: list[int]
    percent: str
    ap_ppr: str
    rop_count: str
    simple_count: str

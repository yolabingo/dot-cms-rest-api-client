from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="UpgradeTaskForm")


@attr.s(auto_attribs=True)
class UpgradeTaskForm:
    """
    Attributes:
        upgrade_task_class (str):
    """

    upgrade_task_class: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        upgrade_task_class = self.upgrade_task_class

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "upgradeTaskClass": upgrade_task_class,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        upgrade_task_class = d.pop("upgradeTaskClass")

        upgrade_task_form = cls(
            upgrade_task_class=upgrade_task_class,
        )

        upgrade_task_form.additional_properties = d
        return upgrade_task_form

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties

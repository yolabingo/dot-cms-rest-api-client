from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.permission import Permission
from ..models.workflow_scheme_import_export_object_view import WorkflowSchemeImportExportObjectView
from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkflowSchemeImportObjectForm")


@attr.s(auto_attribs=True)
class WorkflowSchemeImportObjectForm:
    """
    Attributes:
        workflow_import_object (WorkflowSchemeImportExportObjectView):
        workflow_object (Union[Unset, WorkflowSchemeImportExportObjectView]):
        permissions (Union[Unset, List[Permission]]):
    """

    workflow_import_object: WorkflowSchemeImportExportObjectView
    workflow_object: Union[Unset, WorkflowSchemeImportExportObjectView] = UNSET
    permissions: Union[Unset, List[Permission]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        workflow_import_object = self.workflow_import_object.to_dict()

        workflow_object: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.workflow_object, Unset):
            workflow_object = self.workflow_object.to_dict()

        permissions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = []
            for permissions_item_data in self.permissions:
                permissions_item = permissions_item_data.to_dict()

                permissions.append(permissions_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "workflowImportObject": workflow_import_object,
            }
        )
        if workflow_object is not UNSET:
            field_dict["workflowObject"] = workflow_object
        if permissions is not UNSET:
            field_dict["permissions"] = permissions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        workflow_import_object = WorkflowSchemeImportExportObjectView.from_dict(d.pop("workflowImportObject"))

        _workflow_object = d.pop("workflowObject", UNSET)
        workflow_object: Union[Unset, WorkflowSchemeImportExportObjectView]
        if isinstance(_workflow_object, Unset):
            workflow_object = UNSET
        else:
            workflow_object = WorkflowSchemeImportExportObjectView.from_dict(_workflow_object)

        permissions = []
        _permissions = d.pop("permissions", UNSET)
        for permissions_item_data in _permissions or []:
            permissions_item = Permission.from_dict(permissions_item_data)

            permissions.append(permissions_item)

        workflow_scheme_import_object_form = cls(
            workflow_import_object=workflow_import_object,
            workflow_object=workflow_object,
            permissions=permissions,
        )

        workflow_scheme_import_object_form.additional_properties = d
        return workflow_scheme_import_object_form

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

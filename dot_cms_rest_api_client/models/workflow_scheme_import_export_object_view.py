from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.system_action_workflow_action_mapping import SystemActionWorkflowActionMapping
from ..models.workflow_action import WorkflowAction
from ..models.workflow_action_class import WorkflowActionClass
from ..models.workflow_action_class_parameter import WorkflowActionClassParameter
from ..models.workflow_scheme import WorkflowScheme
from ..models.workflow_scheme_import_export_object_view_action_steps_item import (
    WorkflowSchemeImportExportObjectViewActionStepsItem,
)
from ..models.workflow_step import WorkflowStep
from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkflowSchemeImportExportObjectView")


@attr.s(auto_attribs=True)
class WorkflowSchemeImportExportObjectView:
    """
    Attributes:
        version (Union[Unset, str]):
        schemes (Union[Unset, List[WorkflowScheme]]):
        steps (Union[Unset, List[WorkflowStep]]):
        actions (Union[Unset, List[WorkflowAction]]):
        action_steps (Union[Unset, List[WorkflowSchemeImportExportObjectViewActionStepsItem]]):
        action_classes (Union[Unset, List[WorkflowActionClass]]):
        action_class_params (Union[Unset, List[WorkflowActionClassParameter]]):
        scheme_system_action_workflow_action_mappings (Union[Unset, List[SystemActionWorkflowActionMapping]]):
    """

    version: Union[Unset, str] = UNSET
    schemes: Union[Unset, List[WorkflowScheme]] = UNSET
    steps: Union[Unset, List[WorkflowStep]] = UNSET
    actions: Union[Unset, List[WorkflowAction]] = UNSET
    action_steps: Union[Unset, List[WorkflowSchemeImportExportObjectViewActionStepsItem]] = UNSET
    action_classes: Union[Unset, List[WorkflowActionClass]] = UNSET
    action_class_params: Union[Unset, List[WorkflowActionClassParameter]] = UNSET
    scheme_system_action_workflow_action_mappings: Union[Unset, List[SystemActionWorkflowActionMapping]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        version = self.version
        schemes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.schemes, Unset):
            schemes = []
            for schemes_item_data in self.schemes:
                schemes_item = schemes_item_data.to_dict()

                schemes.append(schemes_item)

        steps: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.steps, Unset):
            steps = []
            for steps_item_data in self.steps:
                steps_item = steps_item_data.to_dict()

                steps.append(steps_item)

        actions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.actions, Unset):
            actions = []
            for actions_item_data in self.actions:
                actions_item = actions_item_data.to_dict()

                actions.append(actions_item)

        action_steps: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.action_steps, Unset):
            action_steps = []
            for action_steps_item_data in self.action_steps:
                action_steps_item = action_steps_item_data.to_dict()

                action_steps.append(action_steps_item)

        action_classes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.action_classes, Unset):
            action_classes = []
            for action_classes_item_data in self.action_classes:
                action_classes_item = action_classes_item_data.to_dict()

                action_classes.append(action_classes_item)

        action_class_params: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.action_class_params, Unset):
            action_class_params = []
            for action_class_params_item_data in self.action_class_params:
                action_class_params_item = action_class_params_item_data.to_dict()

                action_class_params.append(action_class_params_item)

        scheme_system_action_workflow_action_mappings: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.scheme_system_action_workflow_action_mappings, Unset):
            scheme_system_action_workflow_action_mappings = []
            for (
                scheme_system_action_workflow_action_mappings_item_data
            ) in self.scheme_system_action_workflow_action_mappings:
                scheme_system_action_workflow_action_mappings_item = (
                    scheme_system_action_workflow_action_mappings_item_data.to_dict()
                )

                scheme_system_action_workflow_action_mappings.append(scheme_system_action_workflow_action_mappings_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if version is not UNSET:
            field_dict["version"] = version
        if schemes is not UNSET:
            field_dict["schemes"] = schemes
        if steps is not UNSET:
            field_dict["steps"] = steps
        if actions is not UNSET:
            field_dict["actions"] = actions
        if action_steps is not UNSET:
            field_dict["actionSteps"] = action_steps
        if action_classes is not UNSET:
            field_dict["actionClasses"] = action_classes
        if action_class_params is not UNSET:
            field_dict["actionClassParams"] = action_class_params
        if scheme_system_action_workflow_action_mappings is not UNSET:
            field_dict["schemeSystemActionWorkflowActionMappings"] = scheme_system_action_workflow_action_mappings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        version = d.pop("version", UNSET)

        schemes = []
        _schemes = d.pop("schemes", UNSET)
        for schemes_item_data in _schemes or []:
            schemes_item = WorkflowScheme.from_dict(schemes_item_data)

            schemes.append(schemes_item)

        steps = []
        _steps = d.pop("steps", UNSET)
        for steps_item_data in _steps or []:
            steps_item = WorkflowStep.from_dict(steps_item_data)

            steps.append(steps_item)

        actions = []
        _actions = d.pop("actions", UNSET)
        for actions_item_data in _actions or []:
            actions_item = WorkflowAction.from_dict(actions_item_data)

            actions.append(actions_item)

        action_steps = []
        _action_steps = d.pop("actionSteps", UNSET)
        for action_steps_item_data in _action_steps or []:
            action_steps_item = WorkflowSchemeImportExportObjectViewActionStepsItem.from_dict(action_steps_item_data)

            action_steps.append(action_steps_item)

        action_classes = []
        _action_classes = d.pop("actionClasses", UNSET)
        for action_classes_item_data in _action_classes or []:
            action_classes_item = WorkflowActionClass.from_dict(action_classes_item_data)

            action_classes.append(action_classes_item)

        action_class_params = []
        _action_class_params = d.pop("actionClassParams", UNSET)
        for action_class_params_item_data in _action_class_params or []:
            action_class_params_item = WorkflowActionClassParameter.from_dict(action_class_params_item_data)

            action_class_params.append(action_class_params_item)

        scheme_system_action_workflow_action_mappings = []
        _scheme_system_action_workflow_action_mappings = d.pop("schemeSystemActionWorkflowActionMappings", UNSET)
        for scheme_system_action_workflow_action_mappings_item_data in (
            _scheme_system_action_workflow_action_mappings or []
        ):
            scheme_system_action_workflow_action_mappings_item = SystemActionWorkflowActionMapping.from_dict(
                scheme_system_action_workflow_action_mappings_item_data
            )

            scheme_system_action_workflow_action_mappings.append(scheme_system_action_workflow_action_mappings_item)

        workflow_scheme_import_export_object_view = cls(
            version=version,
            schemes=schemes,
            steps=steps,
            actions=actions,
            action_steps=action_steps,
            action_classes=action_classes,
            action_class_params=action_class_params,
            scheme_system_action_workflow_action_mappings=scheme_system_action_workflow_action_mappings,
        )

        workflow_scheme_import_export_object_view.additional_properties = d
        return workflow_scheme_import_export_object_view

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

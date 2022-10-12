import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.field_field_content_type_properties_item import FieldFieldContentTypePropertiesItem
from ..models.story_block_field_data_type import StoryBlockFieldDataType
from ..types import UNSET, Unset

T = TypeVar("T", bound="StoryBlockField")


@attr.s(auto_attribs=True)
class StoryBlockField:
    """
    Attributes:
        clazz (str):
        field_content_type_properties (Union[Unset, List[FieldFieldContentTypePropertiesItem]]):
        searchable (Union[Unset, bool]):
        unique (Union[Unset, bool]):
        indexed (Union[Unset, bool]):
        listed (Union[Unset, bool]):
        read_only (Union[Unset, bool]):
        owner (Union[Unset, str]):
        id (Union[Unset, str]):
        mod_date (Union[Unset, datetime.datetime]):
        name (Union[Unset, str]):
        relation_type (Union[Unset, str]):
        required (Union[Unset, bool]):
        variable (Union[Unset, str]):
        sort_order (Union[Unset, int]):
        values (Union[Unset, str]):
        regex_check (Union[Unset, str]):
        hint (Union[Unset, str]):
        default_value (Union[Unset, str]):
        fixed (Union[Unset, bool]):
        content_type_id (Union[Unset, str]):
        db_column (Union[Unset, str]):
        i_date (Union[Unset, datetime.datetime]):
        data_type (Union[Unset, StoryBlockFieldDataType]):
    """

    clazz: str
    field_content_type_properties: Union[Unset, List[FieldFieldContentTypePropertiesItem]] = UNSET
    searchable: Union[Unset, bool] = UNSET
    unique: Union[Unset, bool] = UNSET
    indexed: Union[Unset, bool] = UNSET
    listed: Union[Unset, bool] = UNSET
    read_only: Union[Unset, bool] = UNSET
    owner: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    mod_date: Union[Unset, datetime.datetime] = UNSET
    name: Union[Unset, str] = UNSET
    relation_type: Union[Unset, str] = UNSET
    required: Union[Unset, bool] = UNSET
    variable: Union[Unset, str] = UNSET
    sort_order: Union[Unset, int] = UNSET
    values: Union[Unset, str] = UNSET
    regex_check: Union[Unset, str] = UNSET
    hint: Union[Unset, str] = UNSET
    default_value: Union[Unset, str] = UNSET
    fixed: Union[Unset, bool] = UNSET
    content_type_id: Union[Unset, str] = UNSET
    db_column: Union[Unset, str] = UNSET
    i_date: Union[Unset, datetime.datetime] = UNSET
    data_type: Union[Unset, StoryBlockFieldDataType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        clazz = self.clazz
        field_content_type_properties: Union[Unset, List[str]] = UNSET
        if not isinstance(self.field_content_type_properties, Unset):
            field_content_type_properties = []
            for field_content_type_properties_item_data in self.field_content_type_properties:
                field_content_type_properties_item = field_content_type_properties_item_data.value

                field_content_type_properties.append(field_content_type_properties_item)

        searchable = self.searchable
        unique = self.unique
        indexed = self.indexed
        listed = self.listed
        read_only = self.read_only
        owner = self.owner
        id = self.id
        mod_date: Union[Unset, str] = UNSET
        if not isinstance(self.mod_date, Unset):
            mod_date = self.mod_date.isoformat()

        name = self.name
        relation_type = self.relation_type
        required = self.required
        variable = self.variable
        sort_order = self.sort_order
        values = self.values
        regex_check = self.regex_check
        hint = self.hint
        default_value = self.default_value
        fixed = self.fixed
        content_type_id = self.content_type_id
        db_column = self.db_column
        i_date: Union[Unset, str] = UNSET
        if not isinstance(self.i_date, Unset):
            i_date = self.i_date.isoformat()

        data_type: Union[Unset, str] = UNSET
        if not isinstance(self.data_type, Unset):
            data_type = self.data_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "clazz": clazz,
            }
        )
        if field_content_type_properties is not UNSET:
            field_dict["fieldContentTypeProperties"] = field_content_type_properties
        if searchable is not UNSET:
            field_dict["searchable"] = searchable
        if unique is not UNSET:
            field_dict["unique"] = unique
        if indexed is not UNSET:
            field_dict["indexed"] = indexed
        if listed is not UNSET:
            field_dict["listed"] = listed
        if read_only is not UNSET:
            field_dict["readOnly"] = read_only
        if owner is not UNSET:
            field_dict["owner"] = owner
        if id is not UNSET:
            field_dict["id"] = id
        if mod_date is not UNSET:
            field_dict["modDate"] = mod_date
        if name is not UNSET:
            field_dict["name"] = name
        if relation_type is not UNSET:
            field_dict["relationType"] = relation_type
        if required is not UNSET:
            field_dict["required"] = required
        if variable is not UNSET:
            field_dict["variable"] = variable
        if sort_order is not UNSET:
            field_dict["sortOrder"] = sort_order
        if values is not UNSET:
            field_dict["values"] = values
        if regex_check is not UNSET:
            field_dict["regexCheck"] = regex_check
        if hint is not UNSET:
            field_dict["hint"] = hint
        if default_value is not UNSET:
            field_dict["defaultValue"] = default_value
        if fixed is not UNSET:
            field_dict["fixed"] = fixed
        if content_type_id is not UNSET:
            field_dict["contentTypeId"] = content_type_id
        if db_column is not UNSET:
            field_dict["dbColumn"] = db_column
        if i_date is not UNSET:
            field_dict["iDate"] = i_date
        if data_type is not UNSET:
            field_dict["dataType"] = data_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        clazz = d.pop("clazz")

        field_content_type_properties = []
        _field_content_type_properties = d.pop("fieldContentTypeProperties", UNSET)
        for field_content_type_properties_item_data in _field_content_type_properties or []:
            field_content_type_properties_item = FieldFieldContentTypePropertiesItem(
                field_content_type_properties_item_data
            )

            field_content_type_properties.append(field_content_type_properties_item)

        searchable = d.pop("searchable", UNSET)

        unique = d.pop("unique", UNSET)

        indexed = d.pop("indexed", UNSET)

        listed = d.pop("listed", UNSET)

        read_only = d.pop("readOnly", UNSET)

        owner = d.pop("owner", UNSET)

        id = d.pop("id", UNSET)

        _mod_date = d.pop("modDate", UNSET)
        mod_date: Union[Unset, datetime.datetime]
        if isinstance(_mod_date, Unset):
            mod_date = UNSET
        else:
            mod_date = isoparse(_mod_date)

        name = d.pop("name", UNSET)

        relation_type = d.pop("relationType", UNSET)

        required = d.pop("required", UNSET)

        variable = d.pop("variable", UNSET)

        sort_order = d.pop("sortOrder", UNSET)

        values = d.pop("values", UNSET)

        regex_check = d.pop("regexCheck", UNSET)

        hint = d.pop("hint", UNSET)

        default_value = d.pop("defaultValue", UNSET)

        fixed = d.pop("fixed", UNSET)

        content_type_id = d.pop("contentTypeId", UNSET)

        db_column = d.pop("dbColumn", UNSET)

        _i_date = d.pop("iDate", UNSET)
        i_date: Union[Unset, datetime.datetime]
        if isinstance(_i_date, Unset):
            i_date = UNSET
        else:
            i_date = isoparse(_i_date)

        _data_type = d.pop("dataType", UNSET)
        data_type: Union[Unset, StoryBlockFieldDataType]
        if isinstance(_data_type, Unset):
            data_type = UNSET
        else:
            data_type = StoryBlockFieldDataType(_data_type)

        story_block_field = cls(
            clazz=clazz,
            field_content_type_properties=field_content_type_properties,
            searchable=searchable,
            unique=unique,
            indexed=indexed,
            listed=listed,
            read_only=read_only,
            owner=owner,
            id=id,
            mod_date=mod_date,
            name=name,
            relation_type=relation_type,
            required=required,
            variable=variable,
            sort_order=sort_order,
            values=values,
            regex_check=regex_check,
            hint=hint,
            default_value=default_value,
            fixed=fixed,
            content_type_id=content_type_id,
            db_column=db_column,
            i_date=i_date,
            data_type=data_type,
        )

        story_block_field.additional_properties = d
        return story_block_field

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

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.template_layout_view import TemplateLayoutView
from ..types import UNSET, Unset

T = TypeVar("T", bound="TemplateForm")


@attr.s(auto_attribs=True)
class TemplateForm:
    """
    Attributes:
        title (str):
        site_id (Union[Unset, str]):
        identifier (Union[Unset, str]):
        inode (Union[Unset, str]):
        body (Union[Unset, str]):
        selectedimage (Union[Unset, str]):
        image (Union[Unset, str]):
        drawed (Union[Unset, bool]):
        show_on_menu (Union[Unset, bool]):
        drawed_body (Union[Unset, str]):
        count_add_container (Union[Unset, int]):
        count_containers (Union[Unset, int]):
        head_code (Union[Unset, str]):
        theme (Union[Unset, str]):
        theme_name (Union[Unset, str]):
        footer (Union[Unset, str]):
        friendly_name (Union[Unset, str]):
        header (Union[Unset, str]):
        name (Union[Unset, str]):
        sort_order (Union[Unset, int]):
        header_check (Union[Unset, bool]):
        footer_check (Union[Unset, bool]):
        layout (Union[Unset, TemplateLayoutView]):
    """

    title: str
    site_id: Union[Unset, str] = UNSET
    identifier: Union[Unset, str] = UNSET
    inode: Union[Unset, str] = UNSET
    body: Union[Unset, str] = UNSET
    selectedimage: Union[Unset, str] = UNSET
    image: Union[Unset, str] = UNSET
    drawed: Union[Unset, bool] = UNSET
    show_on_menu: Union[Unset, bool] = UNSET
    drawed_body: Union[Unset, str] = UNSET
    count_add_container: Union[Unset, int] = UNSET
    count_containers: Union[Unset, int] = UNSET
    head_code: Union[Unset, str] = UNSET
    theme: Union[Unset, str] = UNSET
    theme_name: Union[Unset, str] = UNSET
    footer: Union[Unset, str] = UNSET
    friendly_name: Union[Unset, str] = UNSET
    header: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    sort_order: Union[Unset, int] = UNSET
    header_check: Union[Unset, bool] = UNSET
    footer_check: Union[Unset, bool] = UNSET
    layout: Union[Unset, TemplateLayoutView] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        title = self.title
        site_id = self.site_id
        identifier = self.identifier
        inode = self.inode
        body = self.body
        selectedimage = self.selectedimage
        image = self.image
        drawed = self.drawed
        show_on_menu = self.show_on_menu
        drawed_body = self.drawed_body
        count_add_container = self.count_add_container
        count_containers = self.count_containers
        head_code = self.head_code
        theme = self.theme
        theme_name = self.theme_name
        footer = self.footer
        friendly_name = self.friendly_name
        header = self.header
        name = self.name
        sort_order = self.sort_order
        header_check = self.header_check
        footer_check = self.footer_check
        layout: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.layout, Unset):
            layout = self.layout.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
            }
        )
        if site_id is not UNSET:
            field_dict["siteId"] = site_id
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if inode is not UNSET:
            field_dict["inode"] = inode
        if body is not UNSET:
            field_dict["body"] = body
        if selectedimage is not UNSET:
            field_dict["selectedimage"] = selectedimage
        if image is not UNSET:
            field_dict["image"] = image
        if drawed is not UNSET:
            field_dict["drawed"] = drawed
        if show_on_menu is not UNSET:
            field_dict["showOnMenu"] = show_on_menu
        if drawed_body is not UNSET:
            field_dict["drawedBody"] = drawed_body
        if count_add_container is not UNSET:
            field_dict["countAddContainer"] = count_add_container
        if count_containers is not UNSET:
            field_dict["countContainers"] = count_containers
        if head_code is not UNSET:
            field_dict["headCode"] = head_code
        if theme is not UNSET:
            field_dict["theme"] = theme
        if theme_name is not UNSET:
            field_dict["themeName"] = theme_name
        if footer is not UNSET:
            field_dict["footer"] = footer
        if friendly_name is not UNSET:
            field_dict["friendlyName"] = friendly_name
        if header is not UNSET:
            field_dict["header"] = header
        if name is not UNSET:
            field_dict["name"] = name
        if sort_order is not UNSET:
            field_dict["sortOrder"] = sort_order
        if header_check is not UNSET:
            field_dict["headerCheck"] = header_check
        if footer_check is not UNSET:
            field_dict["footerCheck"] = footer_check
        if layout is not UNSET:
            field_dict["layout"] = layout

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        title = d.pop("title")

        site_id = d.pop("siteId", UNSET)

        identifier = d.pop("identifier", UNSET)

        inode = d.pop("inode", UNSET)

        body = d.pop("body", UNSET)

        selectedimage = d.pop("selectedimage", UNSET)

        image = d.pop("image", UNSET)

        drawed = d.pop("drawed", UNSET)

        show_on_menu = d.pop("showOnMenu", UNSET)

        drawed_body = d.pop("drawedBody", UNSET)

        count_add_container = d.pop("countAddContainer", UNSET)

        count_containers = d.pop("countContainers", UNSET)

        head_code = d.pop("headCode", UNSET)

        theme = d.pop("theme", UNSET)

        theme_name = d.pop("themeName", UNSET)

        footer = d.pop("footer", UNSET)

        friendly_name = d.pop("friendlyName", UNSET)

        header = d.pop("header", UNSET)

        name = d.pop("name", UNSET)

        sort_order = d.pop("sortOrder", UNSET)

        header_check = d.pop("headerCheck", UNSET)

        footer_check = d.pop("footerCheck", UNSET)

        _layout = d.pop("layout", UNSET)
        layout: Union[Unset, TemplateLayoutView]
        if isinstance(_layout, Unset):
            layout = UNSET
        else:
            layout = TemplateLayoutView.from_dict(_layout)

        template_form = cls(
            title=title,
            site_id=site_id,
            identifier=identifier,
            inode=inode,
            body=body,
            selectedimage=selectedimage,
            image=image,
            drawed=drawed,
            show_on_menu=show_on_menu,
            drawed_body=drawed_body,
            count_add_container=count_add_container,
            count_containers=count_containers,
            head_code=head_code,
            theme=theme,
            theme_name=theme_name,
            footer=footer,
            friendly_name=friendly_name,
            header=header,
            name=name,
            sort_order=sort_order,
            header_check=header_check,
            footer_check=footer_check,
            layout=layout,
        )

        template_form.additional_properties = d
        return template_form

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

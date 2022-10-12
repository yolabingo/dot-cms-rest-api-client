from typing import Any, Dict

import httpx

from ...client import Client
from ...models.move_fields_form import MoveFieldsForm
from ...types import Response


def _get_kwargs(
    type_id_or_var_name: str,
    *,
    client: Client,
    json_body: MoveFieldsForm,
) -> Dict[str, Any]:
    url = "{}/v3/contenttype/{typeIdOrVarName}/fields/move".format(client.base_url, typeIdOrVarName=type_id_or_var_name)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _build_response(*, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=None,
    )


def sync_detailed(
    type_id_or_var_name: str,
    *,
    client: Client,
    json_body: MoveFieldsForm,
) -> Response[Any]:
    """
    Args:
        type_id_or_var_name (str):
        json_body (MoveFieldsForm):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        type_id_or_var_name=type_id_or_var_name,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    type_id_or_var_name: str,
    *,
    client: Client,
    json_body: MoveFieldsForm,
) -> Response[Any]:
    """
    Args:
        type_id_or_var_name (str):
        json_body (MoveFieldsForm):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        type_id_or_var_name=type_id_or_var_name,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)

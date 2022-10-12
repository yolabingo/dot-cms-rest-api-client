from typing import Any, Dict

import httpx

from ...client import Client
from ...types import Response


def _get_kwargs(
    type_id_or_var_name: str,
    field_var: str,
    *,
    client: Client,
    json_body: str,
) -> Dict[str, Any]:
    url = "{}/v2/contenttype/{typeIdOrVarName}/fields/var/{fieldVar}".format(
        client.base_url, typeIdOrVarName=type_id_or_var_name, fieldVar=field_var
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body

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
    field_var: str,
    *,
    client: Client,
    json_body: str,
) -> Response[Any]:
    """
    Args:
        type_id_or_var_name (str):
        field_var (str):
        json_body (str):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        type_id_or_var_name=type_id_or_var_name,
        field_var=field_var,
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
    field_var: str,
    *,
    client: Client,
    json_body: str,
) -> Response[Any]:
    """
    Args:
        type_id_or_var_name (str):
        field_var (str):
        json_body (str):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        type_id_or_var_name=type_id_or_var_name,
        field_var=field_var,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)

from typing import Any, Dict

import httpx

from ...client import Client
from ...types import Response


def _get_kwargs(
    type_id: str,
    field_var: str,
    field_var_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/v1/contenttype/{typeId}/fields/var/{fieldVar}/variables/id/{fieldVarId}".format(
        client.base_url, typeId=type_id, fieldVar=field_var, fieldVarId=field_var_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "delete",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _build_response(*, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=None,
    )


def sync_detailed(
    type_id: str,
    field_var: str,
    field_var_id: str,
    *,
    client: Client,
) -> Response[Any]:
    """
    Args:
        type_id (str):
        field_var (str):
        field_var_id (str):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        type_id=type_id,
        field_var=field_var,
        field_var_id=field_var_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    type_id: str,
    field_var: str,
    field_var_id: str,
    *,
    client: Client,
) -> Response[Any]:
    """
    Args:
        type_id (str):
        field_var (str):
        field_var_id (str):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        type_id=type_id,
        field_var=field_var,
        field_var_id=field_var_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)

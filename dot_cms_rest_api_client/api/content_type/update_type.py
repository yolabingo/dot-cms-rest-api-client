from typing import Any, Dict

import httpx

from ...client import Client
from ...models.content_type_form import ContentTypeForm
from ...types import Response


def _get_kwargs(
    id_or_var: str,
    *,
    client: Client,
    json_body: ContentTypeForm,
) -> Dict[str, Any]:
    url = "{}/v1/contenttype/id/{idOrVar}".format(client.base_url, idOrVar=id_or_var)

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
    id_or_var: str,
    *,
    client: Client,
    json_body: ContentTypeForm,
) -> Response[Any]:
    """
    Args:
        id_or_var (str):
        json_body (ContentTypeForm):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id_or_var=id_or_var,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    id_or_var: str,
    *,
    client: Client,
    json_body: ContentTypeForm,
) -> Response[Any]:
    """
    Args:
        id_or_var (str):
        json_body (ContentTypeForm):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id_or_var=id_or_var,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)

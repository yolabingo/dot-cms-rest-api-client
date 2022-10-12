from typing import Any, Dict

import httpx

from ...client import Client
from ...models.rest_condition import RestCondition
from ...types import Response


def _get_kwargs(
    site_id: str,
    condition_id: str,
    *,
    client: Client,
    json_body: RestCondition,
) -> Dict[str, Any]:
    url = "{}/v1/sites/{siteId}/ruleengine/conditions/{conditionId}".format(
        client.base_url, siteId=site_id, conditionId=condition_id
    )

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
    site_id: str,
    condition_id: str,
    *,
    client: Client,
    json_body: RestCondition,
) -> Response[Any]:
    """
    Args:
        site_id (str):
        condition_id (str):
        json_body (RestCondition):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        site_id=site_id,
        condition_id=condition_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    site_id: str,
    condition_id: str,
    *,
    client: Client,
    json_body: RestCondition,
) -> Response[Any]:
    """
    Args:
        site_id (str):
        condition_id (str):
        json_body (RestCondition):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        site_id=site_id,
        condition_id=condition_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)

from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.response_site_variables_entity_view import ResponseSiteVariablesEntityView
from ...types import Response


def _get_kwargs(
    site_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/v1/site/variable/{siteId}".format(client.base_url, siteId=site_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, ResponseSiteVariablesEntityView]]:
    if response.status_code == 200:
        response_200 = ResponseSiteVariablesEntityView.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, ResponseSiteVariablesEntityView]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    site_id: str,
    *,
    client: Client,
) -> Response[Union[Any, ResponseSiteVariablesEntityView]]:
    """Retrieve the Site Variables for a site

    Args:
        site_id (str):

    Returns:
        Response[Union[Any, ResponseSiteVariablesEntityView]]
    """

    kwargs = _get_kwargs(
        site_id=site_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    site_id: str,
    *,
    client: Client,
) -> Optional[Union[Any, ResponseSiteVariablesEntityView]]:
    """Retrieve the Site Variables for a site

    Args:
        site_id (str):

    Returns:
        Response[Union[Any, ResponseSiteVariablesEntityView]]
    """

    return sync_detailed(
        site_id=site_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    site_id: str,
    *,
    client: Client,
) -> Response[Union[Any, ResponseSiteVariablesEntityView]]:
    """Retrieve the Site Variables for a site

    Args:
        site_id (str):

    Returns:
        Response[Union[Any, ResponseSiteVariablesEntityView]]
    """

    kwargs = _get_kwargs(
        site_id=site_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    site_id: str,
    *,
    client: Client,
) -> Optional[Union[Any, ResponseSiteVariablesEntityView]]:
    """Retrieve the Site Variables for a site

    Args:
        site_id (str):

    Returns:
        Response[Union[Any, ResponseSiteVariablesEntityView]]
    """

    return (
        await asyncio_detailed(
            site_id=site_id,
            client=client,
        )
    ).parsed

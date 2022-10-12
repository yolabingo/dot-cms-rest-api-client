from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.fire_multiple_action_default_system_action import FireMultipleActionDefaultSystemAction
from ...models.fire_multiple_action_form import FireMultipleActionForm
from ...models.response_entity_view import ResponseEntityView
from ...types import Response


def _get_kwargs(
    system_action: FireMultipleActionDefaultSystemAction,
    *,
    client: Client,
    json_body: FireMultipleActionForm,
) -> Dict[str, Any]:
    url = "{}/v1/workflow/actions/default/fire/{systemAction}".format(client.base_url, systemAction=system_action)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, ResponseEntityView]]:
    if response.status_code == 200:
        response_200 = ResponseEntityView.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, ResponseEntityView]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    system_action: FireMultipleActionDefaultSystemAction,
    *,
    client: Client,
    json_body: FireMultipleActionForm,
) -> Response[Union[Any, ResponseEntityView]]:
    """Fire default action by name on multiple contents

    Args:
        system_action (FireMultipleActionDefaultSystemAction):
        json_body (FireMultipleActionForm):

    Returns:
        Response[Union[Any, ResponseEntityView]]
    """

    kwargs = _get_kwargs(
        system_action=system_action,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    system_action: FireMultipleActionDefaultSystemAction,
    *,
    client: Client,
    json_body: FireMultipleActionForm,
) -> Optional[Union[Any, ResponseEntityView]]:
    """Fire default action by name on multiple contents

    Args:
        system_action (FireMultipleActionDefaultSystemAction):
        json_body (FireMultipleActionForm):

    Returns:
        Response[Union[Any, ResponseEntityView]]
    """

    return sync_detailed(
        system_action=system_action,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    system_action: FireMultipleActionDefaultSystemAction,
    *,
    client: Client,
    json_body: FireMultipleActionForm,
) -> Response[Union[Any, ResponseEntityView]]:
    """Fire default action by name on multiple contents

    Args:
        system_action (FireMultipleActionDefaultSystemAction):
        json_body (FireMultipleActionForm):

    Returns:
        Response[Union[Any, ResponseEntityView]]
    """

    kwargs = _get_kwargs(
        system_action=system_action,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    system_action: FireMultipleActionDefaultSystemAction,
    *,
    client: Client,
    json_body: FireMultipleActionForm,
) -> Optional[Union[Any, ResponseEntityView]]:
    """Fire default action by name on multiple contents

    Args:
        system_action (FireMultipleActionDefaultSystemAction):
        json_body (FireMultipleActionForm):

    Returns:
        Response[Union[Any, ResponseEntityView]]
    """

    return (
        await asyncio_detailed(
            system_action=system_action,
            client=client,
            json_body=json_body,
        )
    ).parsed

# Copyright (c) Microsoft Corporation.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import pathlib
import sys
import typing

if sys.version_info >= (3, 8):  # pragma: no cover
    from typing import Literal
else:  # pragma: no cover
    from typing_extensions import Literal

from playwright._impl._accessibility import Accessibility as AccessibilityImpl
from playwright._impl._api_structures import Cookie, ResourceTiming, StorageState
from playwright._impl._api_types import (
    DeviceDescriptor,
    FilePayload,
    FloatRect,
    Geolocation,
    PdfMargins,
    ProxySettings,
    SourceLocation,
)
from playwright._impl._browser import Browser as BrowserImpl
from playwright._impl._browser_context import BrowserContext as BrowserContextImpl
from playwright._impl._browser_type import BrowserType as BrowserTypeImpl
from playwright._impl._cdp_session import CDPSession as CDPSessionImpl
from playwright._impl._chromium_browser_context import (
    ChromiumBrowserContext as ChromiumBrowserContextImpl,
)
from playwright._impl._console_message import ConsoleMessage as ConsoleMessageImpl
from playwright._impl._dialog import Dialog as DialogImpl
from playwright._impl._download import Download as DownloadImpl
from playwright._impl._element_handle import ElementHandle as ElementHandleImpl
from playwright._impl._file_chooser import FileChooser as FileChooserImpl
from playwright._impl._frame import Frame as FrameImpl
from playwright._impl._input import Keyboard as KeyboardImpl
from playwright._impl._input import Mouse as MouseImpl
from playwright._impl._input import Touchscreen as TouchscreenImpl
from playwright._impl._js_handle import JSHandle as JSHandleImpl
from playwright._impl._logger import log_api
from playwright._impl._network import Request as RequestImpl
from playwright._impl._network import Response as ResponseImpl
from playwright._impl._network import Route as RouteImpl
from playwright._impl._network import WebSocket as WebSocketImpl
from playwright._impl._page import BindingCall as BindingCallImpl
from playwright._impl._page import Page as PageImpl
from playwright._impl._page import Worker as WorkerImpl
from playwright._impl._playwright import Playwright as PlaywrightImpl
from playwright._impl._selectors import Selectors as SelectorsImpl
from playwright._impl._sync_base import EventContextManager, SyncBase, mapping
from playwright._impl._video import Video as VideoImpl

NoneType = type(None)


class Request(SyncBase):
    def __init__(self, obj: RequestImpl):
        super().__init__(obj)

    @property
    def url(self) -> str:
        """Request.url

        URL of the request.

        Returns
        -------
        str
        """
        return mapping.from_maybe_impl(self._impl_obj.url)

    @property
    def resource_type(self) -> str:
        """Request.resource_type

        Contains the request's resource type as it was perceived by the rendering engine. ResourceType will be one of the
        following: `document`, `stylesheet`, `image`, `media`, `font`, `script`, `texttrack`, `xhr`, `fetch`, `eventsource`,
        `websocket`, `manifest`, `other`.

        Returns
        -------
        str
        """
        return mapping.from_maybe_impl(self._impl_obj.resource_type)

    @property
    def method(self) -> str:
        """Request.method

        Request's method (GET, POST, etc.)

        Returns
        -------
        str
        """
        return mapping.from_maybe_impl(self._impl_obj.method)

    @property
    def post_data(self) -> typing.Union[str, NoneType]:
        """Request.post_data

        Request's post body, if any.

        Returns
        -------
        Union[str, NoneType]
        """
        return mapping.from_maybe_impl(self._impl_obj.post_data)

    @property
    def post_data_json(self) -> typing.Union[typing.Dict, NoneType]:
        """Request.post_data_json

        Returns parsed request's body for `form-urlencoded` and JSON as a fallback if any.

        When the response is `application/x-www-form-urlencoded` then a key/value object of the values will be returned.
        Otherwise it will be parsed as JSON.

        Returns
        -------
        Union[Dict, NoneType]
        """
        return mapping.from_maybe_impl(self._impl_obj.post_data_json)

    @property
    def post_data_buffer(self) -> typing.Union[bytes, NoneType]:
        """Request.post_data_buffer

        Request's post body in a binary form, if any.

        Returns
        -------
        Union[bytes, NoneType]
        """
        return mapping.from_maybe_impl(self._impl_obj.post_data_buffer)

    @property
    def headers(self) -> typing.Dict[str, str]:
        """Request.headers

        An object with HTTP headers associated with the request. All header names are lower-case.

        Returns
        -------
        Dict[str, str]
        """
        return mapping.from_maybe_impl(self._impl_obj.headers)

    @property
    def frame(self) -> "Frame":
        """Request.frame

        Returns the `Frame` that initiated this request.

        Returns
        -------
        Frame
        """
        return mapping.from_impl(self._impl_obj.frame)

    @property
    def is_navigation_request(self) -> bool:
        """Request.is_navigation_request

        Whether this request is driving frame's navigation.

        Returns
        -------
        bool
        """
        return mapping.from_maybe_impl(self._impl_obj.is_navigation_request)

    @property
    def redirected_from(self) -> typing.Union["Request", NoneType]:
        """Request.redirected_from

        Request that was redirected by the server to this one, if any.

        When the server responds with a redirect, Playwright creates a new `Request` object. The two requests are connected by
        `redirectedFrom()` and `redirectedTo()` methods. When multiple server redirects has happened, it is possible to
        construct the whole redirect chain by repeatedly calling `redirectedFrom()`.

        For example, if the website `http://example.com` redirects to `https://example.com`:

        If the website `https://google.com` has no redirects:

        Returns
        -------
        Union[Request, NoneType]
        """
        return mapping.from_impl_nullable(self._impl_obj.redirected_from)

    @property
    def redirected_to(self) -> typing.Union["Request", NoneType]:
        """Request.redirected_to

        New request issued by the browser if the server responded with redirect.

        This method is the opposite of `request.redirected_from()`:

        Returns
        -------
        Union[Request, NoneType]
        """
        return mapping.from_impl_nullable(self._impl_obj.redirected_to)

    @property
    def failure(self) -> typing.Union[str, NoneType]:
        """Request.failure

        The method returns `null` unless this request has failed, as reported by `requestfailed` event.

        Example of logging of all the failed requests:

        Returns
        -------
        Union[str, NoneType]
        """
        return mapping.from_maybe_impl(self._impl_obj.failure)

    @property
    def timing(self) -> "ResourceTiming":
        """Request.timing

        Returns resource timing information for given request. Most of the timing values become available upon the response,
        `responseEnd` becomes available when request finishes. Find more information at
        [Resource Timing API](https://developer.mozilla.org/en-US/docs/Web/API/PerformanceResourceTiming).

        Returns
        -------
        {startTime: float, domainLookupStart: float, domainLookupEnd: float, connectStart: float, secureConnectionStart: float, connectEnd: float, requestStart: float, responseStart: float, responseEnd: float}
        """
        return mapping.from_impl(self._impl_obj.timing)

    def response(self) -> typing.Union["Response", NoneType]:
        """Request.response

        Returns the matching `Response` object, or `null` if the response was not received due to error.

        Returns
        -------
        Union[Response, NoneType]
        """

        try:
            log_api("=> request.response started")
            result = mapping.from_impl_nullable(self._sync(self._impl_obj.response()))
            log_api("<= request.response succeded")
            return result
        except Exception as e:
            log_api("<= request.response failed")
            raise e


mapping.register(RequestImpl, Request)


class Response(SyncBase):
    def __init__(self, obj: ResponseImpl):
        super().__init__(obj)

    @property
    def url(self) -> str:
        """Response.url

        Contains the URL of the response.

        Returns
        -------
        str
        """
        return mapping.from_maybe_impl(self._impl_obj.url)

    @property
    def ok(self) -> bool:
        """Response.ok

        Contains a boolean stating whether the response was successful (status in the range 200-299) or not.

        Returns
        -------
        bool
        """
        return mapping.from_maybe_impl(self._impl_obj.ok)

    @property
    def status(self) -> int:
        """Response.status

        Contains the status code of the response (e.g., 200 for a success).

        Returns
        -------
        int
        """
        return mapping.from_maybe_impl(self._impl_obj.status)

    @property
    def status_text(self) -> str:
        """Response.status_text

        Contains the status text of the response (e.g. usually an "OK" for a success).

        Returns
        -------
        str
        """
        return mapping.from_maybe_impl(self._impl_obj.status_text)

    @property
    def headers(self) -> typing.Dict[str, str]:
        """Response.headers

        Returns the object with HTTP headers associated with the response. All header names are lower-case.

        Returns
        -------
        Dict[str, str]
        """
        return mapping.from_maybe_impl(self._impl_obj.headers)

    @property
    def request(self) -> "Request":
        """Response.request

        Returns the matching `Request` object.

        Returns
        -------
        Request
        """
        return mapping.from_impl(self._impl_obj.request)

    @property
    def frame(self) -> "Frame":
        """Response.frame

        Returns the `Frame` that initiated this response.

        Returns
        -------
        Frame
        """
        return mapping.from_impl(self._impl_obj.frame)

    def finished(self) -> typing.Union[str, NoneType]:
        """Response.finished

        Waits for this response to finish, returns failure error if request failed.

        Returns
        -------
        Union[str, NoneType]
        """

        try:
            log_api("=> response.finished started")
            result = mapping.from_maybe_impl(self._sync(self._impl_obj.finished()))
            log_api("<= response.finished succeded")
            return result
        except Exception as e:
            log_api("<= response.finished failed")
            raise e

    def body(self) -> bytes:
        """Response.body

        Returns the buffer with response body.

        Returns
        -------
        bytes
        """

        try:
            log_api("=> response.body started")
            result = mapping.from_maybe_impl(self._sync(self._impl_obj.body()))
            log_api("<= response.body succeded")
            return result
        except Exception as e:
            log_api("<= response.body failed")
            raise e

    def text(self) -> str:
        """Response.text

        Returns the text representation of response body.

        Returns
        -------
        str
        """

        try:
            log_api("=> response.text started")
            result = mapping.from_maybe_impl(self._sync(self._impl_obj.text()))
            log_api("<= response.text succeded")
            return result
        except Exception as e:
            log_api("<= response.text failed")
            raise e

    def json(self) -> typing.Union[typing.Dict, typing.List]:
        """Response.json

        Returns the JSON representation of response body.

        This method will throw if the response body is not parsable via `JSON.parse`.

        Returns
        -------
        Union[Dict, List]
        """

        try:
            log_api("=> response.json started")
            result = mapping.from_maybe_impl(self._sync(self._impl_obj.json()))
            log_api("<= response.json succeded")
            return result
        except Exception as e:
            log_api("<= response.json failed")
            raise e


mapping.register(ResponseImpl, Response)


class Route(SyncBase):
    def __init__(self, obj: RouteImpl):
        super().__init__(obj)

    @property
    def request(self) -> "Request":
        """Route.request

        A request to be routed.

        Returns
        -------
        Request
        """
        return mapping.from_impl(self._impl_obj.request)

    def abort(self, error_code: str = None) -> NoneType:
        """Route.abort

        Aborts the route's request.

        Parameters
        ----------
        error_code : Union[str, NoneType]
            Optional error code. Defaults to `failed`, could be one of the following:
            - `'aborted'` - An operation was aborted (due to user action)
            - `'accessdenied'` - Permission to access a resource, other than the network, was denied
            - `'addressunreachable'` - The IP address is unreachable. This usually means that there is no route to the specified
              host or network.
            - `'blockedbyclient'` - The client chose to block the request.
            - `'blockedbyresponse'` - The request failed because the response was delivered along with requirements which are not
              met ('X-Frame-Options' and 'Content-Security-Policy' ancestor checks, for instance).
            - `'connectionaborted'` - A connection timed out as a result of not receiving an ACK for data sent.
            - `'connectionclosed'` - A connection was closed (corresponding to a TCP FIN).
            - `'connectionfailed'` - A connection attempt failed.
            - `'connectionrefused'` - A connection attempt was refused.
            - `'connectionreset'` - A connection was reset (corresponding to a TCP RST).
            - `'internetdisconnected'` - The Internet connection has been lost.
            - `'namenotresolved'` - The host name could not be resolved.
            - `'timedout'` - An operation timed out.
            - `'failed'` - A generic failure occurred.
        """

        try:
            log_api("=> route.abort started")
            result = mapping.from_maybe_impl(
                self._sync(self._impl_obj.abort(errorCode=error_code))
            )
            log_api("<= route.abort succeded")
            return result
        except Exception as e:
            log_api("<= route.abort failed")
            raise e

    def fulfill(
        self,
        status: int = None,
        headers: typing.Union[typing.Dict[str, str]] = None,
        body: typing.Union[str, bytes] = None,
        path: typing.Union[str, pathlib.Path] = None,
        content_type: str = None,
    ) -> NoneType:
        """Route.fulfill

        Fulfills route's request with given response.

        An example of fulfilling all requests with 404 responses:

        An example of serving static file:

        Parameters
        ----------
        status : Union[int, NoneType]
            Response status code, defaults to `200`.
        headers : Union[Dict[str, str], NoneType]
            Optional response headers. Header values will be converted to a string.
        body : Union[bytes, str, NoneType]
            Optional response body.
        path : Union[pathlib.Path, str, NoneType]
            Optional file path to respond with. The content type will be inferred from file extension. If `path` is a relative path,
            then it is resolved relative to the current working directory.
        content_type : Union[str, NoneType]
            If set, equals to setting `Content-Type` response header.
        """

        try:
            log_api("=> route.fulfill started")
            result = mapping.from_maybe_impl(
                self._sync(
                    self._impl_obj.fulfill(
                        status=status,
                        headers=mapping.to_impl(headers),
                        body=body,
                        path=path,
                        contentType=content_type,
                    )
                )
            )
            log_api("<= route.fulfill succeded")
            return result
        except Exception as e:
            log_api("<= route.fulfill failed")
            raise e

    def continue_(
        self,
        url: str = None,
        method: str = None,
        headers: typing.Union[typing.Dict[str, str]] = None,
        post_data: typing.Union[str, bytes] = None,
    ) -> NoneType:
        """Route.continue_

        Continues route's request with optional overrides.

        Parameters
        ----------
        url : Union[str, NoneType]
            If set changes the request URL. New URL must have same protocol as original one.
        method : Union[str, NoneType]
            If set changes the request method (e.g. GET or POST)
        headers : Union[Dict[str, str], NoneType]
            If set changes the request HTTP headers. Header values will be converted to a string.
        post_data : Union[bytes, str, NoneType]
            If set changes the post data of request
        """

        try:
            log_api("=> route.continue_ started")
            result = mapping.from_maybe_impl(
                self._sync(
                    self._impl_obj.continue_(
                        url=url,
                        method=method,
                        headers=mapping.to_impl(headers),
                        postData=post_data,
                    )
                )
            )
            log_api("<= route.continue_ succeded")
            return result
        except Exception as e:
            log_api("<= route.continue_ failed")
            raise e


mapping.register(RouteImpl, Route)


class WebSocket(SyncBase):
    def __init__(self, obj: WebSocketImpl):
        super().__init__(obj)

    @property
    def url(self) -> str:
        """WebSocket.url

        Contains the URL of the WebSocket.

        Returns
        -------
        str
        """
        return mapping.from_maybe_impl(self._impl_obj.url)

    def wait_for_event(
        self,
        event: str,
        predicate: typing.Union[typing.Callable[[typing.Any], bool]] = None,
        timeout: float = None,
    ) -> typing.Any:
        """WebSocket.wait_for_event

        Returns the event data value.

        Waits for event to fire and passes its value into the predicate function. Returns when the predicate returns truthy
        value. Will throw an error if the webSocket is closed before the event is fired.

        Parameters
        ----------
        event : str
            Event name, same one would pass into `webSocket.on(event)`.
        predicate : Union[Callable[[Any], bool], NoneType]
            receives the event data and resolves to truthy value when the waiting should resolve.
        timeout : Union[float, NoneType]
            maximum time to wait for in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default
            value can be changed by using the `browser_context.set_default_timeout()`.

        Returns
        -------
        Any
        """

        try:
            log_api("=> web_socket.wait_for_event started")
            result = mapping.from_maybe_impl(
                self._sync(
                    self._impl_obj.wait_for_event(
                        event=event,
                        predicate=self._wrap_handler(predicate),
                        timeout=timeout,
                    )
                )
            )
            log_api("<= web_socket.wait_for_event succeded")
            return result
        except Exception as e:
            log_api("<= web_socket.wait_for_event failed")
            raise e

    def expect_event(
        self,
        event: str,
        predicate: typing.Union[typing.Callable[[typing.Any], bool]] = None,
        timeout: float = None,
    ) -> EventContextManager:
        """WebSocket.expect_event

        Returns context manager that waits for ``event`` to fire upon exit. It passes event's value
        into the ``predicate`` function and waits for the predicate to return a truthy value. Will throw
        an error if the page is closed before the ``event`` is fired.

        with page.expect_event() as event_info:
            page.click("button")
        value = event_info.value

        Parameters
        ----------
        predicate : Optional[typing.Callable[[Any], bool]]
            Predicate receiving event data.
        timeout : Optional[int]
            Maximum wait time in milliseconds, defaults to 30 seconds, pass `0` to disable the timeout.
            The default value can be changed by using the browserContext.set_default_timeout(timeout) or
            page.set_default_timeout(timeout) methods.
        """
        return EventContextManager(
            self, self._impl_obj.wait_for_event(event, predicate, timeout)
        )

    def is_closed(self) -> bool:
        """WebSocket.is_closed

        Indicates that the web socket has been closed.

        Returns
        -------
        bool
        """

        try:
            log_api("=> web_socket.is_closed started")
            result = mapping.from_maybe_impl(self._impl_obj.is_closed())
            log_api("<= web_socket.is_closed succeded")
            return result
        except Exception as e:
            log_api("<= web_socket.is_closed failed")
            raise e


mapping.register(WebSocketImpl, WebSocket)


class Keyboard(SyncBase):
    def __init__(self, obj: KeyboardImpl):
        super().__init__(obj)

    def down(self, key: str) -> NoneType:
        """Keyboard.down

        Dispatches a `keydown` event.

        `key` can specify the intended [keyboardEvent.key](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/key)
        value or a single character to generate the text for. A superset of the `key` values can be found
        [here](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/key/Key_Values). Examples of the keys are:

        `F1` - `F12`, `Digit0`- `Digit9`, `KeyA`- `KeyZ`, `Backquote`, `Minus`, `Equal`, `Backslash`, `Backspace`, `Tab`,
        `Delete`, `Escape`, `ArrowDown`, `End`, `Enter`, `Home`, `Insert`, `PageDown`, `PageUp`, `ArrowRight`, `ArrowUp`, etc.

        Following modification shortcuts are also supported: `Shift`, `Control`, `Alt`, `Meta`, `ShiftLeft`.

        Holding down `Shift` will type the text that corresponds to the `key` in the upper case.

        If `key` is a single character, it is case-sensitive, so the values `a` and `A` will generate different respective
        texts.

        If `key` is a modifier key, `Shift`, `Meta`, `Control`, or `Alt`, subsequent key presses will be sent with that modifier
        active. To release the modifier key, use `keyboard.up()`.

        After the key is pressed once, subsequent calls to `keyboard.down()` will have
        [repeat](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/repeat) set to true. To release the key, use
        `keyboard.up()`.

        > **NOTE** Modifier keys DO influence `keyboard.down`. Holding down `Shift` will type the text in upper case.

        Parameters
        ----------
        key : str
            Name of the key to press or a character to generate, such as `ArrowLeft` or `a`.
        """

        try:
            log_api("=> keyboard.down started")
            result = mapping.from_maybe_impl(self._sync(self._impl_obj.down(key=key)))
            log_api("<= keyboard.down succeded")
            return result
        except Exception as e:
            log_api("<= keyboard.down failed")
            raise e

    def up(self, key: str) -> NoneType:
        """Keyboard.up

        Dispatches a `keyup` event.

        Parameters
        ----------
        key : str
            Name of the key to press or a character to generate, such as `ArrowLeft` or `a`.
        """

        try:
            log_api("=> keyboard.up started")
            result = mapping.from_maybe_impl(self._sync(self._impl_obj.up(key=key)))
            log_api("<= keyboard.up succeded")
            return result
        except Exception as e:
            log_api("<= keyboard.up failed")
            raise e

    def insert_text(self, text: str) -> NoneType:
        """Keyboard.insert_text

        Dispatches only `input` event, does not emit the `keydown`, `keyup` or `keypress` events.

        > **NOTE** Modifier keys DO NOT effect `keyboard.insertText`. Holding down `Shift` will not type the text in upper case.

        Parameters
        ----------
        text : str
            Sets input to the specified text value.
        """

        try:
            log_api("=> keyboard.insert_text started")
            result = mapping.from_maybe_impl(
                self._sync(self._impl_obj.insert_text(text=text))
            )
            log_api("<= keyboard.insert_text succeded")
            return result
        except Exception as e:
            log_api("<= keyboard.insert_text failed")
            raise e

    def type(self, text: str, delay: float = None) -> NoneType:
        """Keyboard.type

        Sends a `keydown`, `keypress`/`input`, and `keyup` event for each character in the text.

        To press a special key, like `Control` or `ArrowDown`, use `keyboard.press()`.

        > **NOTE** Modifier keys DO NOT effect `keyboard.type`. Holding down `Shift` will not type the text in upper case.

        Parameters
        ----------
        text : str
            A text to type into a focused element.
        delay : Union[float, NoneType]
            Time to wait between key presses in milliseconds. Defaults to 0.
        """

        try:
            log_api("=> keyboard.type started")
            result = mapping.from_maybe_impl(
                self._sync(self._impl_obj.type(text=text, delay=delay))
            )
            log_api("<= keyboard.type succeded")
            return result
        except Exception as e:
            log_api("<= keyboard.type failed")
            raise e

    def press(self, key: str, delay: float = None) -> NoneType:
        """Keyboard.press

        `key` can specify the intended [keyboardEvent.key](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/key)
        value or a single character to generate the text for. A superset of the `key` values can be found
        [here](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/key/Key_Values). Examples of the keys are:

        `F1` - `F12`, `Digit0`- `Digit9`, `KeyA`- `KeyZ`, `Backquote`, `Minus`, `Equal`, `Backslash`, `Backspace`, `Tab`,
        `Delete`, `Escape`, `ArrowDown`, `End`, `Enter`, `Home`, `Insert`, `PageDown`, `PageUp`, `ArrowRight`, `ArrowUp`, etc.

        Following modification shortcuts are also supported: `Shift`, `Control`, `Alt`, `Meta`, `ShiftLeft`.

        Holding down `Shift` will type the text that corresponds to the `key` in the upper case.

        If `key` is a single character, it is case-sensitive, so the values `a` and `A` will generate different respective
        texts.

        Shortcuts such as `key: "Control+o"` or `key: "Control+Shift+T"` are supported as well. When speficied with the
        modifier, modifier is pressed and being held while the subsequent key is being pressed.

        Shortcut for `keyboard.down()` and `keyboard.up()`.

        Parameters
        ----------
        key : str
            Name of the key to press or a character to generate, such as `ArrowLeft` or `a`.
        delay : Union[float, NoneType]
            Time to wait between `keydown` and `keyup` in milliseconds. Defaults to 0.
        """

        try:
            log_api("=> keyboard.press started")
            result = mapping.from_maybe_impl(
                self._sync(self._impl_obj.press(key=key, delay=delay))
            )
            log_api("<= keyboard.press succeded")
            return result
        except Exception as e:
            log_api("<= keyboard.press failed")
            raise e


mapping.register(KeyboardImpl, Keyboard)


class Mouse(SyncBase):
    def __init__(self, obj: MouseImpl):
        super().__init__(obj)

    def move(self, x: float, y: float, steps: int = None) -> NoneType:
        """Mouse.move

        Dispatches a `mousemove` event.

        Parameters
        ----------
        x : float
        y : float
        steps : Union[int, NoneType]
            defaults to 1. Sends intermediate `mousemove` events.
        """

        try:
            log_api("=> mouse.move started")
            result = mapping.from_maybe_impl(
                self._sync(self._impl_obj.move(x=x, y=y, steps=steps))
            )
            log_api("<= mouse.move succeded")
            return result
        except Exception as e:
            log_api("<= mouse.move failed")
            raise e

    def down(
        self, button: Literal["left", "middle", "right"] = None, click_count: int = None
    ) -> NoneType:
        """Mouse.down

        Dispatches a `mousedown` event.

        Parameters
        ----------
        button : Union["left", "middle", "right", NoneType]
            Defaults to `left`.
        click_count : Union[int, NoneType]
            defaults to 1. See [UIEvent.detail].
        """

        try:
            log_api("=> mouse.down started")
            result = mapping.from_maybe_impl(
                self._sync(self._impl_obj.down(button=button, clickCount=click_count))
            )
            log_api("<= mouse.down succeded")
            return result
        except Exception as e:
            log_api("<= mouse.down failed")
            raise e

    def up(
        self, button: Literal["left", "middle", "right"] = None, click_count: int = None
    ) -> NoneType:
        """Mouse.up

        Dispatches a `mouseup` event.

        Parameters
        ----------
        button : Union["left", "middle", "right", NoneType]
            Defaults to `left`.
        click_count : Union[int, NoneType]
            defaults to 1. See [UIEvent.detail].
        """

        try:
            log_api("=> mouse.up started")
            result = mapping.from_maybe_impl(
                self._sync(self._impl_obj.up(button=button, clickCount=click_count))
            )
            log_api("<= mouse.up succeded")
            return result
        except Exception as e:
            log_api("<= mouse.up failed")
            raise e

    def click(
        self,
        x: float,
        y: float,
        delay: float = None,
        button: Literal["left", "middle", "right"] = None,
        click_count: int = None,
    ) -> NoneType:
        """Mouse.click

        Shortcut for `mouse.move()`, `mouse.down()`, `mouse.up()`.

        Parameters
        ----------
        x : float
        y : float
        delay : Union[float, NoneType]
            Time to wait between `mousedown` and `mouseup` in milliseconds. Defaults to 0.
        button : Union["left", "middle", "right", NoneType]
            Defaults to `left`.
        click_count : Union[int, NoneType]
            defaults to 1. See [UIEvent.detail].
        """

        try:
            log_api("=> mouse.click started")
            result = mapping.from_maybe_impl(
                self._sync(
                    self._impl_obj.click(
                        x=x, y=y, delay=delay, button=button, clickCount=click_count
                    )
                )
            )
            log_api("<= mouse.click succeded")
            return result
        except Exception as e:
            log_api("<= mouse.click failed")
            raise e

    def dblclick(
        self,
        x: float,
        y: float,
        delay: float = None,
        button: Literal["left", "middle", "right"] = None,
    ) -> NoneType:
        """Mouse.dblclick

        Shortcut for `mouse.move()`, `mouse.down()`, `mouse.up()`, `mouse.down()` and
        `mouse.up()`.

        Parameters
        ----------
        x : float
        y : float
        delay : Union[float, NoneType]
            Time to wait between `mousedown` and `mouseup` in milliseconds. Defaults to 0.
        button : Union["left", "middle", "right", NoneType]
            Defaults to `left`.
        """

        try:
            log_api("=> mouse.dblclick started")
            result = mapping.from_maybe_impl(
                self._sync(
                    self._impl_obj.dblclick(x=x, y=y, delay=delay, button=button)
                )
            )
            log_api("<= mouse.dblclick succeded")
            return result
        except Exception as e:
            log_api("<= mouse.dblclick failed")
            raise e


mapping.register(MouseImpl, Mouse)


class Touchscreen(SyncBase):
    def __init__(self, obj: TouchscreenImpl):
        super().__init__(obj)

    def tap(self, x: float, y: float) -> NoneType:
        """Touchscreen.tap

        Dispatches a `touchstart` and `touchend` event with a single touch at the position (`x`,`y`).

        Parameters
        ----------
        x : float
        y : float
        """

        try:
            log_api("=> touchscreen.tap started")
            result = mapping.from_maybe_impl(self._sync(self._impl_obj.tap(x=x, y=y)))
            log_api("<= touchscreen.tap succeded")
            return result
        except Exception as e:
            log_api("<= touchscreen.tap failed")
            raise e


mapping.register(TouchscreenImpl, Touchscreen)


class JSHandle(SyncBase):
    def __init__(self, obj: JSHandleImpl):
        super().__init__(obj)

    def evaluate(
        self, expression: str, arg: typing.Any = None, force_expr: bool = None
    ) -> typing.Any:
        """JSHandle.evaluate

        Returns the return value of `pageFunction`

        This method passes this handle as the first argument to `pageFunction`.

        If `pageFunction` returns a [Promise], then `handle.evaluate` would wait for the promise to resolve and return its
        value.

        Examples:

        Parameters
        ----------
        expression : str
            Function to be evaluated in browser context
        force_expr : bool
            Whether to treat given expression as JavaScript evaluate expression, even though it looks like an arrow function
        arg : Union[Any, NoneType]
            Optional argument to pass to `pageFunction`

        Returns
        -------
        Any
        """

        try:
            log_api("=> js_handle.evaluate started")
            result = mapping.from_maybe_impl(
                self._sync(
                    self._impl_obj.evaluate(
                        expression=expression,
                        arg=mapping.to_impl(arg),
                        force_expr=force_expr,
                    )
                )
            )
            log_api("<= js_handle.evaluate succeded")
            return result
        except Exception as e:
            log_api("<= js_handle.evaluate failed")
            raise e

    def evaluate_handle(
        self, expression: str, arg: typing.Any = None, force_expr: bool = None
    ) -> "JSHandle":
        """JSHandle.evaluate_handle

        Returns the return value of `pageFunction` as in-page object (JSHandle).

        This method passes this handle as the first argument to `pageFunction`.

        The only difference between `jsHandle.evaluate` and `jsHandle.evaluateHandle` is that `jsHandle.evaluateHandle` returns
        in-page object (JSHandle).

        If the function passed to the `jsHandle.evaluateHandle` returns a [Promise], then `jsHandle.evaluateHandle` would wait
        for the promise to resolve and return its value.

        See `page.evaluate_handle()` for more details.

        Parameters
        ----------
        expression : str
            Function to be evaluated
        force_expr : bool
            Whether to treat given expression as JavaScript evaluate expression, even though it looks like an arrow function
        arg : Union[Any, NoneType]
            Optional argument to pass to `pageFunction`

        Returns
        -------
        JSHandle
        """

        try:
            log_api("=> js_handle.evaluate_handle started")
            result = mapping.from_impl(
                self._sync(
                    self._impl_obj.evaluate_handle(
                        expression=expression,
                        arg=mapping.to_impl(arg),
                        force_expr=force_expr,
                    )
                )
            )
            log_api("<= js_handle.evaluate_handle succeded")
            return result
        except Exception as e:
            log_api("<= js_handle.evaluate_handle failed")
            raise e

    def get_property(self, property_name: str) -> "JSHandle":
        """JSHandle.get_property

        Fetches a single property from the referenced object.

        Parameters
        ----------
        property_name : str
            property to get

        Returns
        -------
        JSHandle
        """

        try:
            log_api("=> js_handle.get_property started")
            result = mapping.from_impl(
                self._sync(self._impl_obj.get_property(propertyName=property_name))
            )
            log_api("<= js_handle.get_property succeded")
            return result
        except Exception as e:
            log_api("<= js_handle.get_property failed")
            raise e

    def get_properties(self) -> typing.Dict[str, "JSHandle"]:
        """JSHandle.get_properties

        The method returns a map with **own property names** as keys and JSHandle instances for the property values.

        Returns
        -------
        Dict[str, JSHandle]
        """

        try:
            log_api("=> js_handle.get_properties started")
            result = mapping.from_impl_dict(self._sync(self._impl_obj.get_properties()))
            log_api("<= js_handle.get_properties succeded")
            return result
        except Exception as e:
            log_api("<= js_handle.get_properties failed")
            raise e

    def as_element(self) -> typing.Union["ElementHandle", NoneType]:
        """JSHandle.as_element

        Returns either `null` or the object handle itself, if the object handle is an instance of `ElementHandle`.

        Returns
        -------
        Union[ElementHandle, NoneType]
        """

        try:
            log_api("=> js_handle.as_element started")
            result = mapping.from_impl_nullable(self._impl_obj.as_element())
            log_api("<= js_handle.as_element succeded")
            return result
        except Exception as e:
            log_api("<= js_handle.as_element failed")
            raise e

    def dispose(self) -> NoneType:
        """JSHandle.dispose

        The `jsHandle.dispose` method stops referencing the element handle.
        """

        try:
            log_api("=> js_handle.dispose started")
            result = mapping.from_maybe_impl(self._sync(self._impl_obj.dispose()))
            log_api("<= js_handle.dispose succeded")
            return result
        except Exception as e:
            log_api("<= js_handle.dispose failed")
            raise e

    def json_value(self) -> typing.Any:
        """JSHandle.json_value

        Returns a JSON representation of the object. If the object has a `toJSON` function, it **will not be called**.

        > **NOTE** The method will return an empty JSON object if the referenced object is not stringifiable. It will throw an
        error if the object has circular references.

        Returns
        -------
        Any
        """

        try:
            log_api("=> js_handle.json_value started")
            result = mapping.from_maybe_impl(self._sync(self._impl_obj.json_value()))
            log_api("<= js_handle.json_value succeded")
            return result
        except Exception as e:
            log_api("<= js_handle.json_value failed")
            raise e


mapping.register(JSHandleImpl, JSHandle)


class ElementHandle(JSHandle):
    def __init__(self, obj: ElementHandleImpl):
        super().__init__(obj)

    def as_element(self) -> typing.Union["ElementHandle", NoneType]:
        """ElementHandle.as_element

        Returns either `null` or the object handle itself, if the object handle is an instance of `ElementHandle`.

        Returns
        -------
        Union[ElementHandle, NoneType]
        """

        try:
            log_api("=> element_handle.as_element started")
            result = mapping.from_impl_nullable(self._impl_obj.as_element())
            log_api("<= element_handle.as_element succeded")
            return result
        except Exception as e:
            log_api("<= element_handle.as_element failed")
            raise e

    def owner_frame(self) -> typing.Union["Frame", NoneType]:
        """ElementHandle.owner_frame

        Returns the frame containing the given element.

        Returns
        -------
        Union[Frame, NoneType]
        """

        try:
            log_api("=> element_handle.owner_frame started")
            result = mapping.from_impl_nullable(
                self._sync(self._impl_obj.owner_frame())
            )
            log_api("<= element_handle.owner_frame succeded")
            return result
        except Exception as e:
            log_api("<= element_handle.owner_frame failed")
            raise e

    def content_frame(self) -> typing.Union["Frame", NoneType]:
        """ElementHandle.content_frame

        Returns the content frame for element handles referencing iframe nodes, or `null` otherwise

        Returns
        -------
        Union[Frame, NoneType]
        """

        try:
            log_api("=> element_handle.content_frame started")
            result = mapping.from_impl_nullable(
                self._sync(self._impl_obj.content_frame())
            )
            log_api("<= element_handle.content_frame succeded")
            return result
        except Exception as e:
            log_api("<= element_handle.content_frame failed")
            raise e

    def get_attribute(self, name: str) -> typing.Union[str, NoneType]:
        """ElementHandle.get_attribute

        Returns element attribute value.

        Parameters
        ----------
        name : str
            Attribute name to get the value for.

        Returns
        -------
        Union[str, NoneType]
        """

        try:
            log_api("=> element_handle.get_attribute started")
            result = mapping.from_maybe_impl(
                self._sync(self._impl_obj.get_attribute(name=name))
            )
            log_api("<= element_handle.get_attribute succeded")
            return result
        except Exception as e:
            log_api("<= element_handle.get_attribute failed")
            raise e

    def text_content(self) -> typing.Union[str, NoneType]:
        """ElementHandle.text_content

        Returns the `node.textContent`.

        Returns
        -------
        Union[str, NoneType]
        """

        try:
            log_api("=> element_handle.text_content started")
            result = mapping.from_maybe_impl(self._sync(self._impl_obj.text_content()))
            log_api("<= element_handle.text_content succeded")
            return result
        except Exception as e:
            log_api("<= element_handle.text_content failed")
            raise e

    def inner_text(self) -> str:
        """ElementHandle.inner_text

        Returns the `element.innerText`.

        Returns
        -------
        str
        """

        try:
            log_api("=> element_handle.inner_text started")
            result = mapping.from_maybe_impl(self._sync(self._impl_obj.inner_text()))
            log_api("<= element_handle.inner_text succeded")
            return result
        except Exception as e:
            log_api("<= element_handle.inner_text failed")
            raise e

    def inner_html(self) -> str:
        """ElementHandle.inner_html

        Returns the `element.innerHTML`.

        Returns
        -------
        str
        """

        try:
            log_api("=> element_handle.inner_html started")
            result = mapping.from_maybe_impl(self._sync(self._impl_obj.inner_html()))
            log_api("<= element_handle.inner_html succeded")
            return result
        except Exception as e:
            log_api("<= element_handle.inner_html failed")
            raise e

    def dispatch_event(self, type: str, event_init: typing.Dict = None) -> NoneType:
        """ElementHandle.dispatch_event

        The snippet below dispatches the `click` event on the element. Regardless of the visibility state of the elment, `click`
        is dispatched. This is equivalend to calling
        [element.click()](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/click).

        Under the hood, it creates an instance of an event based on the given `type`, initializes it with `eventInit` properties
        and dispatches it on the element. Events are `composed`, `cancelable` and bubble by default.

        Since `eventInit` is event-specific, please refer to the events documentation for the lists of initial properties:
        - [DragEvent](https://developer.mozilla.org/en-US/docs/Web/API/DragEvent/DragEvent)
        - [FocusEvent](https://developer.mozilla.org/en-US/docs/Web/API/FocusEvent/FocusEvent)
        - [KeyboardEvent](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/KeyboardEvent)
        - [MouseEvent](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/MouseEvent)
        - [PointerEvent](https://developer.mozilla.org/en-US/docs/Web/API/PointerEvent/PointerEvent)
        - [TouchEvent](https://developer.mozilla.org/en-US/docs/Web/API/TouchEvent/TouchEvent)
        - [Event](https://developer.mozilla.org/en-US/docs/Web/API/Event/Event)

        You can also specify `JSHandle` as the property value if you want live objects to be passed into the event:

        Parameters
        ----------
        type : str
            DOM event type: `"click"`, `"dragstart"`, etc.
        event_init : Union[Dict, NoneType]
            Optional event-specific initialization properties.
        """

        try:
            log_api("=> element_handle.dispatch_event started")
            result = mapping.from_maybe_impl(
                self._sync(
                    self._impl_obj.dispatch_event(
                        type=type, eventInit=mapping.to_impl(event_init)
                    )
                )
            )
            log_api("<= element_handle.dispatch_event succeded")
            return result
        except Exception as e:
            log_api("<= element_handle.dispatch_event failed")
            raise e

    def scroll_into_view_if_needed(self, timeout: float = None) -> NoneType:
        """ElementHandle.scroll_into_view_if_needed

        This method waits for [actionability](./actionability.md) checks, then tries to scroll element into view, unless it is
        completely visible as defined by
        [IntersectionObserver](https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API)'s ```ratio```.

        Throws when `elementHandle` does not point to an element
        [connected](https://developer.mozilla.org/en-US/docs/Web/API/Node/isConnected) to a Document or a ShadowRoot.

        Parameters
        ----------
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        """

        try:
            log_api("=> element_handle.scroll_into_view_if_needed started")
            result = mapping.from_maybe_impl(
                self._sync(self._impl_obj.scroll_into_view_if_needed(timeout=timeout))
            )
            log_api("<= element_handle.scroll_into_view_if_needed succeded")
            return result
        except Exception as e:
            log_api("<= element_handle.scroll_into_view_if_needed failed")
            raise e

    def hover(
        self,
        modifiers: typing.Union[
            typing.List[Literal["Alt", "Control", "Meta", "Shift"]]
        ] = None,
        position: typing.Union[typing.Tuple[float, float]] = None,
        timeout: float = None,
        force: bool = None,
    ) -> NoneType:
        """ElementHandle.hover

        This method hovers over the element by performing the following steps:
        1. Wait for [actionability](./actionability.md) checks on the element, unless `force` option is set.
        1. Scroll the element into view if needed.
        1. Use `page.mouse` to hover over the center of the element, or the specified `position`.
        1. Wait for initiated navigations to either succeed or fail, unless `noWaitAfter` option is set.

        If the element is detached from the DOM at any moment during the action, this method rejects.

        When all steps combined have not finished during the specified `timeout`, this method rejects with a `TimeoutError`.
        Passing zero timeout disables this.

        Parameters
        ----------
        modifiers : Union[List[Union["Alt", "Control", "Meta", "Shift"]], NoneType]
            Modifier keys to press. Ensures that only these modifiers are pressed during the operation, and then restores current
            modifiers back. If not specified, currently pressed modifiers are used.
        position : Union[typing.Tuple[float, float], NoneType]
            A point to use relative to the top-left corner of element padding box. If not specified, uses some visible point of the
            element.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        force : Union[bool, NoneType]
            Whether to bypass the [actionability](./actionability.md) checks. Defaults to `false`.
        """

        try:
            log_api("=> element_handle.hover started")
            result = mapping.from_maybe_impl(
                self._sync(
                    self._impl_obj.hover(
                        modifiers=modifiers,
                        position=position,
                        timeout=timeout,
                        force=force,
                    )
                )
            )
            log_api("<= element_handle.hover succeded")
            return result
        except Exception as e:
            log_api("<= element_handle.hover failed")
            raise e

    def click(
        self,
        modifiers: typing.Union[
            typing.List[Literal["Alt", "Control", "Meta", "Shift"]]
        ] = None,
        position: typing.Union[typing.Tuple[float, float]] = None,
        delay: float = None,
        button: Literal["left", "middle", "right"] = None,
        click_count: int = None,
        timeout: float = None,
        force: bool = None,
        no_wait_after: bool = None,
    ) -> NoneType:
        """ElementHandle.click

        This method clicks the element by performing the following steps:
        1. Wait for [actionability](./actionability.md) checks on the element, unless `force` option is set.
        1. Scroll the element into view if needed.
        1. Use `page.mouse` to click in the center of the element, or the specified `position`.
        1. Wait for initiated navigations to either succeed or fail, unless `noWaitAfter` option is set.

        If the element is detached from the DOM at any moment during the action, this method rejects.

        When all steps combined have not finished during the specified `timeout`, this method rejects with a `TimeoutError`.
        Passing zero timeout disables this.

        Parameters
        ----------
        modifiers : Union[List[Union["Alt", "Control", "Meta", "Shift"]], NoneType]
            Modifier keys to press. Ensures that only these modifiers are pressed during the operation, and then restores current
            modifiers back. If not specified, currently pressed modifiers are used.
        position : Union[typing.Tuple[float, float], NoneType]
            A point to use relative to the top-left corner of element padding box. If not specified, uses some visible point of the
            element.
        delay : Union[float, NoneType]
            Time to wait between `mousedown` and `mouseup` in milliseconds. Defaults to 0.
        button : Union["left", "middle", "right", NoneType]
            Defaults to `left`.
        click_count : Union[int, NoneType]
            defaults to 1. See [UIEvent.detail].
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        force : Union[bool, NoneType]
            Whether to bypass the [actionability](./actionability.md) checks. Defaults to `false`.
        no_wait_after : Union[bool, NoneType]
            Actions that initiate navigations are waiting for these navigations to happen and for pages to start loading. You can
            opt out of waiting via setting this flag. You would only need this option in the exceptional cases such as navigating to
            inaccessible pages. Defaults to `false`.
        """

        try:
            log_api("=> element_handle.click started")
            result = mapping.from_maybe_impl(
                self._sync(
                    self._impl_obj.click(
                        modifiers=modifiers,
                        position=position,
                        delay=delay,
                        button=button,
                        clickCount=click_count,
                        timeout=timeout,
                        force=force,
                        noWaitAfter=no_wait_after,
                    )
                )
            )
            log_api("<= element_handle.click succeded")
            return result
        except Exception as e:
            log_api("<= element_handle.click failed")
            raise e

    def dblclick(
        self,
        modifiers: typing.Union[
            typing.List[Literal["Alt", "Control", "Meta", "Shift"]]
        ] = None,
        position: typing.Union[typing.Tuple[float, float]] = None,
        delay: float = None,
        button: Literal["left", "middle", "right"] = None,
        timeout: float = None,
        force: bool = None,
        no_wait_after: bool = None,
    ) -> NoneType:
        """ElementHandle.dblclick

        This method double clicks the element by performing the following steps:
        1. Wait for [actionability](./actionability.md) checks on the element, unless `force` option is set.
        1. Scroll the element into view if needed.
        1. Use `page.mouse` to double click in the center of the element, or the specified `position`.
        1. Wait for initiated navigations to either succeed or fail, unless `noWaitAfter` option is set. Note that if the
           first click of the `dblclick()` triggers a navigation event, this method will reject.

        If the element is detached from the DOM at any moment during the action, this method rejects.

        When all steps combined have not finished during the specified `timeout`, this method rejects with a `TimeoutError`.
        Passing zero timeout disables this.

        > **NOTE** `elementHandle.dblclick()` dispatches two `click` events and a single `dblclick` event.

        Parameters
        ----------
        modifiers : Union[List[Union["Alt", "Control", "Meta", "Shift"]], NoneType]
            Modifier keys to press. Ensures that only these modifiers are pressed during the operation, and then restores current
            modifiers back. If not specified, currently pressed modifiers are used.
        position : Union[typing.Tuple[float, float], NoneType]
            A point to use relative to the top-left corner of element padding box. If not specified, uses some visible point of the
            element.
        delay : Union[float, NoneType]
            Time to wait between `mousedown` and `mouseup` in milliseconds. Defaults to 0.
        button : Union["left", "middle", "right", NoneType]
            Defaults to `left`.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        force : Union[bool, NoneType]
            Whether to bypass the [actionability](./actionability.md) checks. Defaults to `false`.
        no_wait_after : Union[bool, NoneType]
            Actions that initiate navigations are waiting for these navigations to happen and for pages to start loading. You can
            opt out of waiting via setting this flag. You would only need this option in the exceptional cases such as navigating to
            inaccessible pages. Defaults to `false`.
        """

        try:
            log_api("=> element_handle.dblclick started")
            result = mapping.from_maybe_impl(
                self._sync(
                    self._impl_obj.dblclick(
                        modifiers=modifiers,
                        position=position,
                        delay=delay,
                        button=button,
                        timeout=timeout,
                        force=force,
                        noWaitAfter=no_wait_after,
                    )
                )
            )
            log_api("<= element_handle.dblclick succeded")
            return result
        except Exception as e:
            log_api("<= element_handle.dblclick failed")
            raise e

    def select_option(
        self,
        value: typing.Union[str, typing.List[str]] = None,
        index: typing.Union[int, typing.List[int]] = None,
        label: typing.Union[str, typing.List[str]] = None,
        element: typing.Union["ElementHandle", typing.List["ElementHandle"]] = None,
        timeout: float = None,
        no_wait_after: bool = None,
    ) -> typing.List[str]:
        """ElementHandle.select_option

        Returns the array of option values that have been successfully selected.

        Triggers a `change` and `input` event once all the provided options have been selected. If element is not a `<select>`
        element, the method throws an error.

        Parameters
        ----------
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        no_wait_after : Union[bool, NoneType]
            Actions that initiate navigations are waiting for these navigations to happen and for pages to start loading. You can
            opt out of waiting via setting this flag. You would only need this option in the exceptional cases such as navigating to
            inaccessible pages. Defaults to `false`.

        Returns
        -------
        List[str]
        """

        try:
            log_api("=> element_handle.select_option started")
            result = mapping.from_maybe_impl(
                self._sync(
                    self._impl_obj.select_option(
                        value=value,
                        index=index,
                        label=label,
                        element=mapping.to_impl(element),
                        timeout=timeout,
                        noWaitAfter=no_wait_after,
                    )
                )
            )
            log_api("<= element_handle.select_option succeded")
            return result
        except Exception as e:
            log_api("<= element_handle.select_option failed")
            raise e

    def tap(
        self,
        modifiers: typing.Union[
            typing.List[Literal["Alt", "Control", "Meta", "Shift"]]
        ] = None,
        position: typing.Union[typing.Tuple[float, float]] = None,
        timeout: float = None,
        force: bool = None,
        no_wait_after: bool = None,
    ) -> NoneType:
        """ElementHandle.tap

        This method taps the element by performing the following steps:
        1. Wait for [actionability](./actionability.md) checks on the element, unless `force` option is set.
        1. Scroll the element into view if needed.
        1. Use `page.touchscreen` to tap the center of the element, or the specified `position`.
        1. Wait for initiated navigations to either succeed or fail, unless `noWaitAfter` option is set.

        If the element is detached from the DOM at any moment during the action, this method rejects.

        When all steps combined have not finished during the specified `timeout`, this method rejects with a `TimeoutError`.
        Passing zero timeout disables this.

        > **NOTE** `elementHandle.tap()` requires that the `hasTouch` option of the browser context be set to true.

        Parameters
        ----------
        modifiers : Union[List[Union["Alt", "Control", "Meta", "Shift"]], NoneType]
            Modifier keys to press. Ensures that only these modifiers are pressed during the operation, and then restores current
            modifiers back. If not specified, currently pressed modifiers are used.
        position : Union[typing.Tuple[float, float], NoneType]
            A point to use relative to the top-left corner of element padding box. If not specified, uses some visible point of the
            element.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        force : Union[bool, NoneType]
            Whether to bypass the [actionability](./actionability.md) checks. Defaults to `false`.
        no_wait_after : Union[bool, NoneType]
            Actions that initiate navigations are waiting for these navigations to happen and for pages to start loading. You can
            opt out of waiting via setting this flag. You would only need this option in the exceptional cases such as navigating to
            inaccessible pages. Defaults to `false`.
        """

        try:
            log_api("=> element_handle.tap started")
            result = mapping.from_maybe_impl(
                self._sync(
                    self._impl_obj.tap(
                        modifiers=modifiers,
                        position=position,
                        timeout=timeout,
                        force=force,
                        noWaitAfter=no_wait_after,
                    )
                )
            )
            log_api("<= element_handle.tap succeded")
            return result
        except Exception as e:
            log_api("<= element_handle.tap failed")
            raise e

    def fill(
        self, value: str, timeout: float = None, no_wait_after: bool = None
    ) -> NoneType:
        """ElementHandle.fill

        This method waits for [actionability](./actionability.md) checks, focuses the element, fills it and triggers an `input`
        event after filling. If the element is not an `<input>`, `<textarea>` or `[contenteditable]` element, this method throws
        an error. Note that you can pass an empty string to clear the input field.

        Parameters
        ----------
        value : str
            Value to set for the `<input>`, `<textarea>` or `[contenteditable]` element.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        no_wait_after : Union[bool, NoneType]
            Actions that initiate navigations are waiting for these navigations to happen and for pages to start loading. You can
            opt out of waiting via setting this flag. You would only need this option in the exceptional cases such as navigating to
            inaccessible pages. Defaults to `false`.
        """

        try:
            log_api("=> element_handle.fill started")
            result = mapping.from_maybe_impl(
                self._sync(
                    self._impl_obj.fill(
                        value=value, timeout=timeout, noWaitAfter=no_wait_after
                    )
                )
            )
            log_api("<= element_handle.fill succeded")
            return result
        except Exception as e:
            log_api("<= element_handle.fill failed")
            raise e

    def select_text(self, timeout: float = None) -> NoneType:
        """ElementHandle.select_text

        This method waits for [actionability](./actionability.md) checks, then focuses the element and selects all its text
        content.

        Parameters
        ----------
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        """

        try:
            log_api("=> element_handle.select_text started")
            result = mapping.from_maybe_impl(
                self._sync(self._impl_obj.select_text(timeout=timeout))
            )
            log_api("<= element_handle.select_text succeded")
            return result
        except Exception as e:
            log_api("<= element_handle.select_text failed")
            raise e

    def set_input_files(
        self,
        files: typing.Union[
            str,
            pathlib.Path,
            "FilePayload",
            typing.List[str],
            typing.List[pathlib.Path],
            typing.List["FilePayload"],
        ],
        timeout: float = None,
        no_wait_after: bool = None,
    ) -> NoneType:
        """ElementHandle.set_input_files

        This method expects `elementHandle` to point to an
        [input element](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input).

        Sets the value of the file input to these file paths or files. If some of the `filePaths` are relative paths, then they
        are resolved relative to the the current working directory. For empty array, clears the selected files.

        Parameters
        ----------
        files : Union[List[pathlib.Path], List[str], List[{name: str, mime_type: str, buffer: bytes}], pathlib.Path, str, {name: str, mime_type: str, buffer: bytes}]
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        no_wait_after : Union[bool, NoneType]
            Actions that initiate navigations are waiting for these navigations to happen and for pages to start loading. You can
            opt out of waiting via setting this flag. You would only need this option in the exceptional cases such as navigating to
            inaccessible pages. Defaults to `false`.
        """

        try:
            log_api("=> element_handle.set_input_files started")
            result = mapping.from_maybe_impl(
                self._sync(
                    self._impl_obj.set_input_files(
                        files=files, timeout=timeout, noWaitAfter=no_wait_after
                    )
                )
            )
            log_api("<= element_handle.set_input_files succeded")
            return result
        except Exception as e:
            log_api("<= element_handle.set_input_files failed")
            raise e

    def focus(self) -> NoneType:
        """ElementHandle.focus

        Calls [focus](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/focus) on the element.
        """

        try:
            log_api("=> element_handle.focus started")
            result = mapping.from_maybe_impl(self._sync(self._impl_obj.focus()))
            log_api("<= element_handle.focus succeded")
            return result
        except Exception as e:
            log_api("<= element_handle.focus failed")
            raise e

    def type(
        self,
        text: str,
        delay: float = None,
        timeout: float = None,
        no_wait_after: bool = None,
    ) -> NoneType:
        """ElementHandle.type

        Focuses the element, and then sends a `keydown`, `keypress`/`input`, and `keyup` event for each character in the text.

        To press a special key, like `Control` or `ArrowDown`, use `element_handle.press()`.

        An example of typing into a text field and then submitting the form:

        Parameters
        ----------
        text : str
            A text to type into a focused element.
        delay : Union[float, NoneType]
            Time to wait between key presses in milliseconds. Defaults to 0.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        no_wait_after : Union[bool, NoneType]
            Actions that initiate navigations are waiting for these navigations to happen and for pages to start loading. You can
            opt out of waiting via setting this flag. You would only need this option in the exceptional cases such as navigating to
            inaccessible pages. Defaults to `false`.
        """

        try:
            log_api("=> element_handle.type started")
            result = mapping.from_maybe_impl(
                self._sync(
                    self._impl_obj.type(
                        text=text,
                        delay=delay,
                        timeout=timeout,
                        noWaitAfter=no_wait_after,
                    )
                )
            )
            log_api("<= element_handle.type succeded")
            return result
        except Exception as e:
            log_api("<= element_handle.type failed")
            raise e

    def press(
        self,
        key: str,
        delay: float = None,
        timeout: float = None,
        no_wait_after: bool = None,
    ) -> NoneType:
        """ElementHandle.press

        Focuses the element, and then uses `keyboard.down()` and `keyboard.up()`.

        `key` can specify the intended [keyboardEvent.key](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/key)
        value or a single character to generate the text for. A superset of the `key` values can be found
        [here](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/key/Key_Values). Examples of the keys are:

        `F1` - `F12`, `Digit0`- `Digit9`, `KeyA`- `KeyZ`, `Backquote`, `Minus`, `Equal`, `Backslash`, `Backspace`, `Tab`,
        `Delete`, `Escape`, `ArrowDown`, `End`, `Enter`, `Home`, `Insert`, `PageDown`, `PageUp`, `ArrowRight`, `ArrowUp`, etc.

        Following modification shortcuts are also supported: `Shift`, `Control`, `Alt`, `Meta`, `ShiftLeft`.

        Holding down `Shift` will type the text that corresponds to the `key` in the upper case.

        If `key` is a single character, it is case-sensitive, so the values `a` and `A` will generate different respective
        texts.

        Shortcuts such as `key: "Control+o"` or `key: "Control+Shift+T"` are supported as well. When speficied with the
        modifier, modifier is pressed and being held while the subsequent key is being pressed.

        Parameters
        ----------
        key : str
            Name of the key to press or a character to generate, such as `ArrowLeft` or `a`.
        delay : Union[float, NoneType]
            Time to wait between `keydown` and `keyup` in milliseconds. Defaults to 0.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        no_wait_after : Union[bool, NoneType]
            Actions that initiate navigations are waiting for these navigations to happen and for pages to start loading. You can
            opt out of waiting via setting this flag. You would only need this option in the exceptional cases such as navigating to
            inaccessible pages. Defaults to `false`.
        """

        try:
            log_api("=> element_handle.press started")
            result = mapping.from_maybe_impl(
                self._sync(
                    self._impl_obj.press(
                        key=key, delay=delay, timeout=timeout, noWaitAfter=no_wait_after
                    )
                )
            )
            log_api("<= element_handle.press succeded")
            return result
        except Exception as e:
            log_api("<= element_handle.press failed")
            raise e

    def check(
        self, timeout: float = None, force: bool = None, no_wait_after: bool = None
    ) -> NoneType:
        """ElementHandle.check

        This method checks the element by performing the following steps:
        1. Ensure that element is a checkbox or a radio input. If not, this method rejects. If the element is already
           checked, this method returns immediately.
        1. Wait for [actionability](./actionability.md) checks on the element, unless `force` option is set.
        1. Scroll the element into view if needed.
        1. Use `page.mouse` to click in the center of the element.
        1. Wait for initiated navigations to either succeed or fail, unless `noWaitAfter` option is set.
        1. Ensure that the element is now checked. If not, this method rejects.

        If the element is detached from the DOM at any moment during the action, this method rejects.

        When all steps combined have not finished during the specified `timeout`, this method rejects with a `TimeoutError`.
        Passing zero timeout disables this.

        Parameters
        ----------
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        force : Union[bool, NoneType]
            Whether to bypass the [actionability](./actionability.md) checks. Defaults to `false`.
        no_wait_after : Union[bool, NoneType]
            Actions that initiate navigations are waiting for these navigations to happen and for pages to start loading. You can
            opt out of waiting via setting this flag. You would only need this option in the exceptional cases such as navigating to
            inaccessible pages. Defaults to `false`.
        """

        try:
            log_api("=> element_handle.check started")
            result = mapping.from_maybe_impl(
                self._sync(
                    self._impl_obj.check(
                        timeout=timeout, force=force, noWaitAfter=no_wait_after
                    )
                )
            )
            log_api("<= element_handle.check succeded")
            return result
        except Exception as e:
            log_api("<= element_handle.check failed")
            raise e

    def uncheck(
        self, timeout: float = None, force: bool = None, no_wait_after: bool = None
    ) -> NoneType:
        """ElementHandle.uncheck

        This method checks the element by performing the following steps:
        1. Ensure that element is a checkbox or a radio input. If not, this method rejects. If the element is already
           unchecked, this method returns immediately.
        1. Wait for [actionability](./actionability.md) checks on the element, unless `force` option is set.
        1. Scroll the element into view if needed.
        1. Use `page.mouse` to click in the center of the element.
        1. Wait for initiated navigations to either succeed or fail, unless `noWaitAfter` option is set.
        1. Ensure that the element is now unchecked. If not, this method rejects.

        If the element is detached from the DOM at any moment during the action, this method rejects.

        When all steps combined have not finished during the specified `timeout`, this method rejects with a `TimeoutError`.
        Passing zero timeout disables this.

        Parameters
        ----------
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        force : Union[bool, NoneType]
            Whether to bypass the [actionability](./actionability.md) checks. Defaults to `false`.
        no_wait_after : Union[bool, NoneType]
            Actions that initiate navigations are waiting for these navigations to happen and for pages to start loading. You can
            opt out of waiting via setting this flag. You would only need this option in the exceptional cases such as navigating to
            inaccessible pages. Defaults to `false`.
        """

        try:
            log_api("=> element_handle.uncheck started")
            result = mapping.from_maybe_impl(
                self._sync(
                    self._impl_obj.uncheck(
                        timeout=timeout, force=force, noWaitAfter=no_wait_after
                    )
                )
            )
            log_api("<= element_handle.uncheck succeded")
            return result
        except Exception as e:
            log_api("<= element_handle.uncheck failed")
            raise e

    def bounding_box(self) -> typing.Union["FloatRect", NoneType]:
        """ElementHandle.bounding_box

        This method returns the bounding box of the element, or `null` if the element is not visible. The bounding box is
        calculated relative to the main frame viewport - which is usually the same as the browser window.

        Scrolling affects the returned bonding box, similarly to
        [Element.getBoundingClientRect](https://developer.mozilla.org/en-US/docs/Web/API/Element/getBoundingClientRect). That
        means `x` and/or `y` may be negative.

        Elements from child frames return the bounding box relative to the main frame, unlike the
        [Element.getBoundingClientRect](https://developer.mozilla.org/en-US/docs/Web/API/Element/getBoundingClientRect).

        Assuming the page is static, it is safe to use bounding box coordinates to perform input. For example, the following
        snippet should click the center of the element.

        Returns
        -------
        Union[{x: float, y: float, width: float, height: float}, NoneType]
        """

        try:
            log_api("=> element_handle.bounding_box started")
            result = mapping.from_impl_nullable(
                self._sync(self._impl_obj.bounding_box())
            )
            log_api("<= element_handle.bounding_box succeded")
            return result
        except Exception as e:
            log_api("<= element_handle.bounding_box failed")
            raise e

    def screenshot(
        self,
        timeout: float = None,
        type: Literal["jpeg", "png"] = None,
        path: typing.Union[str, pathlib.Path] = None,
        quality: int = None,
        omit_background: bool = None,
    ) -> bytes:
        """ElementHandle.screenshot

        Returns the buffer with the captured screenshot.

        This method waits for the [actionability](./actionability.md) checks, then scrolls element into view before taking a
        screenshot. If the element is detached from DOM, the method throws an error.

        Parameters
        ----------
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        type : Union["jpeg", "png", NoneType]
            Specify screenshot type, defaults to `png`.
        path : Union[pathlib.Path, str, NoneType]
            The file path to save the image to. The screenshot type will be inferred from file extension. If `path` is a relative
            path, then it is resolved relative to the current working directory. If no path is provided, the image won't be saved to
            the disk.
        quality : Union[int, NoneType]
            The quality of the image, between 0-100. Not applicable to `png` images.
        omit_background : Union[bool, NoneType]
            Hides default white background and allows capturing screenshots with transparency. Not applicable to `jpeg` images.
            Defaults to `false`.

        Returns
        -------
        bytes
        """

        try:
            log_api("=> element_handle.screenshot started")
            result = mapping.from_maybe_impl(
                self._sync(
                    self._impl_obj.screenshot(
                        timeout=timeout,
                        type=type,
                        path=path,
                        quality=quality,
                        omitBackground=omit_background,
                    )
                )
            )
            log_api("<= element_handle.screenshot succeded")
            return result
        except Exception as e:
            log_api("<= element_handle.screenshot failed")
            raise e

    def query_selector(self, selector: str) -> typing.Union["ElementHandle", NoneType]:
        """ElementHandle.query_selector

        The method finds an element matching the specified selector in the `ElementHandle`'s subtree. See
        [Working with selectors](./selectors.md#working-with-selectors) for more details. If no elements match the selector,
        returns `null`.

        Parameters
        ----------
        selector : str
            A selector to query for. See [working with selectors](./selectors.md#working-with-selectors) for more details.

        Returns
        -------
        Union[ElementHandle, NoneType]
        """

        try:
            log_api("=> element_handle.query_selector started")
            result = mapping.from_impl_nullable(
                self._sync(self._impl_obj.query_selector(selector=selector))
            )
            log_api("<= element_handle.query_selector succeded")
            return result
        except Exception as e:
            log_api("<= element_handle.query_selector failed")
            raise e

    def query_selector_all(self, selector: str) -> typing.List["ElementHandle"]:
        """ElementHandle.query_selector_all

        The method finds all elements matching the specified selector in the `ElementHandle`s subtree. See
        [Working with selectors](./selectors.md#working-with-selectors) for more details. If no elements match the selector,
        returns empty array.

        Parameters
        ----------
        selector : str
            A selector to query for. See [working with selectors](./selectors.md#working-with-selectors) for more details.

        Returns
        -------
        List[ElementHandle]
        """

        try:
            log_api("=> element_handle.query_selector_all started")
            result = mapping.from_impl_list(
                self._sync(self._impl_obj.query_selector_all(selector=selector))
            )
            log_api("<= element_handle.query_selector_all succeded")
            return result
        except Exception as e:
            log_api("<= element_handle.query_selector_all failed")
            raise e

    def eval_on_selector(
        self,
        selector: str,
        expression: str,
        arg: typing.Any = None,
        force_expr: bool = None,
    ) -> typing.Any:
        """ElementHandle.eval_on_selector

        Returns the return value of `pageFunction`

        The method finds an element matching the specified selector in the `ElementHandle`s subtree and passes it as a first
        argument to `pageFunction`. See [Working with selectors](./selectors.md#working-with-selectors) for more details. If no
        elements match the selector, the method throws an error.

        If `pageFunction` returns a [Promise], then `frame.$eval` would wait for the promise to resolve and return its value.

        Examples:

        Parameters
        ----------
        selector : str
            A selector to query for. See [working with selectors](./selectors.md#working-with-selectors) for more details.
        expression : str
            Function to be evaluated in browser context
        force_expr : bool
            Whether to treat given expression as JavaScript evaluate expression, even though it looks like an arrow function
        arg : Union[Any, NoneType]
            Optional argument to pass to `pageFunction`

        Returns
        -------
        Any
        """

        try:
            log_api("=> element_handle.eval_on_selector started")
            result = mapping.from_maybe_impl(
                self._sync(
                    self._impl_obj.eval_on_selector(
                        selector=selector,
                        expression=expression,
                        arg=mapping.to_impl(arg),
                        force_expr=force_expr,
                    )
                )
            )
            log_api("<= element_handle.eval_on_selector succeded")
            return result
        except Exception as e:
            log_api("<= element_handle.eval_on_selector failed")
            raise e

    def eval_on_selector_all(
        self,
        selector: str,
        expression: str,
        arg: typing.Any = None,
        force_expr: bool = None,
    ) -> typing.Any:
        """ElementHandle.eval_on_selector_all

        Returns the return value of `pageFunction`

        The method finds all elements matching the specified selector in the `ElementHandle`'s subtree and passes an array of
        matched elements as a first argument to `pageFunction`. See
        [Working with selectors](./selectors.md#working-with-selectors) for more details.

        If `pageFunction` returns a [Promise], then `frame.$$eval` would wait for the promise to resolve and return its value.

        Examples:

        ```html
        <div class="feed">
          <div class="tweet">Hello!</div>
          <div class="tweet">Hi!</div>
        </div>
        ```

        Parameters
        ----------
        selector : str
            A selector to query for. See [working with selectors](./selectors.md#working-with-selectors) for more details.
        expression : str
            Function to be evaluated in browser context
        force_expr : bool
            Whether to treat given expression as JavaScript evaluate expression, even though it looks like an arrow function
        arg : Union[Any, NoneType]
            Optional argument to pass to `pageFunction`

        Returns
        -------
        Any
        """

        try:
            log_api("=> element_handle.eval_on_selector_all started")
            result = mapping.from_maybe_impl(
                self._sync(
                    self._impl_obj.eval_on_selector_all(
                        selector=selector,
                        expression=expression,
                        arg=mapping.to_impl(arg),
                        force_expr=force_expr,
                    )
                )
            )
            log_api("<= element_handle.eval_on_selector_all succeded")
            return result
        except Exception as e:
            log_api("<= element_handle.eval_on_selector_all failed")
            raise e

    def wait_for_element_state(
        self,
        state: Literal["disabled", "enabled", "hidden", "stable", "visible"],
        timeout: float = None,
    ) -> NoneType:
        """ElementHandle.wait_for_element_state

        Returns when the element satisfies the `state`.

        Depending on the `state` parameter, this method waits for one of the [actionability](./actionability.md) checks to pass.
        This method throws when the element is detached while waiting, unless waiting for the `"hidden"` state.
        - `"visible"` Wait until the element is [visible](./actionability.md#visible).
        - `"hidden"` Wait until the element is [not visible](./actionability.md#visible) or
          [not attached](./actionability.md#attached). Note that waiting for hidden does not throw when the element detaches.
        - `"stable"` Wait until the element is both [visible](./actionability.md#visible) and
          [stable](./actionability.md#stable).
        - `"enabled"` Wait until the element is [enabled](./actionability.md#enabled).
        - `"disabled"` Wait until the element is [not enabled](./actionability.md#enabled).

        If the element does not satisfy the condition for the `timeout` milliseconds, this method will throw.

        Parameters
        ----------
        state : Union["disabled", "enabled", "hidden", "stable", "visible"]
            A state to wait for, see below for more details.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        """

        try:
            log_api("=> element_handle.wait_for_element_state started")
            result = mapping.from_maybe_impl(
                self._sync(
                    self._impl_obj.wait_for_element_state(state=state, timeout=timeout)
                )
            )
            log_api("<= element_handle.wait_for_element_state succeded")
            return result
        except Exception as e:
            log_api("<= element_handle.wait_for_element_state failed")
            raise e

    def wait_for_selector(
        self,
        selector: str,
        state: Literal["attached", "detached", "hidden", "visible"] = None,
        timeout: float = None,
    ) -> typing.Union["ElementHandle", NoneType]:
        """ElementHandle.wait_for_selector

        Returns element specified by selector when it satisfies `state` option. Returns `null` if waiting for `hidden` or
        `detached`.

        Wait for the `selector` relative to the element handle to satisfy `state` option (either appear/disappear from dom, or
        become visible/hidden). If at the moment of calling the method `selector` already satisfies the condition, the method
        will return immediately. If the selector doesn't satisfy the condition for the `timeout` milliseconds, the function will
        throw.

        > **NOTE** This method does not work across navigations, use `page.wait_for_selector()` instead.

        Parameters
        ----------
        selector : str
            A selector to query for. See [working with selectors](./selectors.md#working-with-selectors) for more details.
        state : Union["attached", "detached", "hidden", "visible", NoneType]
            Defaults to `'visible'`. Can be either:
            - `'attached'` - wait for element to be present in DOM.
            - `'detached'` - wait for element to not be present in DOM.
            - `'visible'` - wait for element to have non-empty bounding box and no `visibility:hidden`. Note that element without
              any content or with `display:none` has an empty bounding box and is not considered visible.
            - `'hidden'` - wait for element to be either detached from DOM, or have an empty bounding box or `visibility:hidden`.
              This is opposite to the `'visible'` option.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.

        Returns
        -------
        Union[ElementHandle, NoneType]
        """

        try:
            log_api("=> element_handle.wait_for_selector started")
            result = mapping.from_impl_nullable(
                self._sync(
                    self._impl_obj.wait_for_selector(
                        selector=selector, state=state, timeout=timeout
                    )
                )
            )
            log_api("<= element_handle.wait_for_selector succeded")
            return result
        except Exception as e:
            log_api("<= element_handle.wait_for_selector failed")
            raise e


mapping.register(ElementHandleImpl, ElementHandle)


class Accessibility(SyncBase):
    def __init__(self, obj: AccessibilityImpl):
        super().__init__(obj)

    def snapshot(
        self, interesting_only: bool = None, root: "ElementHandle" = None
    ) -> typing.Union[typing.Dict, NoneType]:
        """Accessibility.snapshot

        Captures the current state of the accessibility tree. The returned object represents the root accessible node of the
        page.

        > **NOTE** The Chromium accessibility tree contains nodes that go unused on most platforms and by most screen readers.
        Playwright will discard them as well for an easier to process tree, unless `interestingOnly` is set to `false`.

        An example of dumping the entire accessibility tree:

        An example of logging the focused node's name:

        Parameters
        ----------
        interesting_only : Union[bool, NoneType]
            Prune uninteresting nodes from the tree. Defaults to `true`.
        root : Union[ElementHandle, NoneType]
            The root DOM element for the snapshot. Defaults to the whole page.

        Returns
        -------
        Union[Dict, NoneType]
        """

        try:
            log_api("=> accessibility.snapshot started")
            result = mapping.from_maybe_impl(
                self._sync(
                    self._impl_obj.snapshot(
                        interestingOnly=interesting_only, root=mapping.to_impl(root)
                    )
                )
            )
            log_api("<= accessibility.snapshot succeded")
            return result
        except Exception as e:
            log_api("<= accessibility.snapshot failed")
            raise e


mapping.register(AccessibilityImpl, Accessibility)


class FileChooser(SyncBase):
    def __init__(self, obj: FileChooserImpl):
        super().__init__(obj)

    @property
    def page(self) -> "Page":
        """FileChooser.page

        Returns page this file chooser belongs to.

        Returns
        -------
        Page
        """
        return mapping.from_impl(self._impl_obj.page)

    @property
    def element(self) -> "ElementHandle":
        """FileChooser.element

        Returns input element associated with this file chooser.

        Returns
        -------
        ElementHandle
        """
        return mapping.from_impl(self._impl_obj.element)

    @property
    def is_multiple(self) -> bool:
        """FileChooser.is_multiple

        Returns whether this file chooser accepts multiple files.

        Returns
        -------
        bool
        """
        return mapping.from_maybe_impl(self._impl_obj.is_multiple)

    def set_files(
        self,
        files: typing.Union[
            str, "FilePayload", typing.List[str], typing.List["FilePayload"]
        ],
        timeout: float = None,
        no_wait_after: bool = None,
    ) -> NoneType:
        """FileChooser.set_files

        Sets the value of the file input this chooser is associated with. If some of the `filePaths` are relative paths, then
        they are resolved relative to the the current working directory. For empty array, clears the selected files.

        Parameters
        ----------
        files : Union[List[str], List[{name: str, mime_type: str, buffer: bytes}], str, {name: str, mime_type: str, buffer: bytes}]
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        no_wait_after : Union[bool, NoneType]
            Actions that initiate navigations are waiting for these navigations to happen and for pages to start loading. You can
            opt out of waiting via setting this flag. You would only need this option in the exceptional cases such as navigating to
            inaccessible pages. Defaults to `false`.
        """

        try:
            log_api("=> file_chooser.set_files started")
            result = mapping.from_maybe_impl(
                self._sync(
                    self._impl_obj.set_files(
                        files=files, timeout=timeout, noWaitAfter=no_wait_after
                    )
                )
            )
            log_api("<= file_chooser.set_files succeded")
            return result
        except Exception as e:
            log_api("<= file_chooser.set_files failed")
            raise e


mapping.register(FileChooserImpl, FileChooser)


class Frame(SyncBase):
    def __init__(self, obj: FrameImpl):
        super().__init__(obj)

    @property
    def page(self) -> "Page":
        """Frame.page

        Returns the page containing this frame.

        Returns
        -------
        Page
        """
        return mapping.from_impl(self._impl_obj.page)

    @property
    def name(self) -> str:
        """Frame.name

        Returns frame's name attribute as specified in the tag.

        If the name is empty, returns the id attribute instead.

        > **NOTE** This value is calculated once when the frame is created, and will not update if the attribute is changed
        later.

        Returns
        -------
        str
        """
        return mapping.from_maybe_impl(self._impl_obj.name)

    @property
    def url(self) -> str:
        """Frame.url

        Returns frame's url.

        Returns
        -------
        str
        """
        return mapping.from_maybe_impl(self._impl_obj.url)

    @property
    def parent_frame(self) -> typing.Union["Frame", NoneType]:
        """Frame.parent_frame

        Parent frame, if any. Detached frames and main frames return `null`.

        Returns
        -------
        Union[Frame, NoneType]
        """
        return mapping.from_impl_nullable(self._impl_obj.parent_frame)

    @property
    def child_frames(self) -> typing.List["Frame"]:
        """Frame.child_frames

        Returns
        -------
        List[Frame]
        """
        return mapping.from_impl_list(self._impl_obj.child_frames)

    def goto(
        self,
        url: str,
        timeout: float = None,
        wait_until: Literal["domcontentloaded", "load", "networkidle"] = None,
        referer: str = None,
    ) -> typing.Union["Response", NoneType]:
        """Frame.goto

        Returns the main resource response. In case of multiple redirects, the navigation will resolve with the response of the
        last redirect.

        `frame.goto` will throw an error if:
        - there's an SSL error (e.g. in case of self-signed certificates).
        - target URL is invalid.
        - the `timeout` is exceeded during navigation.
        - the remote server does not respond or is unreachable.
        - the main resource failed to load.

        `frame.goto` will not throw an error when any valid HTTP status code is returned by the remote server, including 404
        "Not Found" and 500 "Internal Server Error".  The status code for such responses can be retrieved by calling
        `response.status()`.

        > **NOTE** `frame.goto` either throws an error or returns a main resource response. The only exceptions are navigation
        to `about:blank` or navigation to the same URL with a different hash, which would succeed and return `null`.
        > **NOTE** Headless mode doesn't support navigation to a PDF document. See the
        [upstream issue](https://bugs.chromium.org/p/chromium/issues/detail?id=761295).

        Parameters
        ----------
        url : str
            URL to navigate frame to. The url should include scheme, e.g. `https://`.
        timeout : Union[float, NoneType]
            Maximum operation time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be
            changed by using the `browser_context.set_default_navigation_timeout()`,
            `browser_context.set_default_timeout()`, `page.set_default_navigation_timeout()` or
            `page.set_default_timeout()` methods.
        wait_until : Union["domcontentloaded", "load", "networkidle", NoneType]
            When to consider operation succeeded, defaults to `load`. Events can be either:
            - `'domcontentloaded'` - consider operation to be finished when the `DOMContentLoaded` event is fired.
            - `'load'` - consider operation to be finished when the `load` event is fired.
            - `'networkidle'` - consider operation to be finished when there are no network connections for at least `500` ms.
        referer : Union[str, NoneType]
            Referer header value. If provided it will take preference over the referer header value set by
            `page.set_extra_http_headers()`.

        Returns
        -------
        Union[Response, NoneType]
        """

        try:
            log_api("=> frame.goto started")
            result = mapping.from_impl_nullable(
                self._sync(
                    self._impl_obj.goto(
                        url=url, timeout=timeout, waitUntil=wait_until, referer=referer
                    )
                )
            )
            log_api("<= frame.goto succeded")
            return result
        except Exception as e:
            log_api("<= frame.goto failed")
            raise e

    def wait_for_navigation(
        self,
        url: typing.Union[str, typing.Pattern, typing.Callable[[str], bool]] = None,
        wait_until: Literal["domcontentloaded", "load", "networkidle"] = None,
        timeout: float = None,
    ) -> typing.Union["Response", NoneType]:
        """Frame.wait_for_navigation

        Returns the main resource response. In case of multiple redirects, the navigation will resolve with the response of the
        last redirect. In case of navigation to a different anchor or navigation due to History API usage, the navigation will
        resolve with `null`.

        This method waits for the frame to navigate to a new URL. It is useful for when you run code which will indirectly cause
        the frame to navigate. Consider this example:

        **NOTE** Usage of the [History API](https://developer.mozilla.org/en-US/docs/Web/API/History_API) to change the URL is
        considered a navigation.

        Parameters
        ----------
        url : Union[Callable[[str], bool], Pattern, str, NoneType]
            URL string, URL regex pattern or predicate receiving [URL] to match while waiting for the navigation.
        wait_until : Union["domcontentloaded", "load", "networkidle", NoneType]
            When to consider operation succeeded, defaults to `load`. Events can be either:
            - `'domcontentloaded'` - consider operation to be finished when the `DOMContentLoaded` event is fired.
            - `'load'` - consider operation to be finished when the `load` event is fired.
            - `'networkidle'` - consider operation to be finished when there are no network connections for at least `500` ms.
        timeout : Union[float, NoneType]
            Maximum operation time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be
            changed by using the `browser_context.set_default_navigation_timeout()`,
            `browser_context.set_default_timeout()`, `page.set_default_navigation_timeout()` or
            `page.set_default_timeout()` methods.

        Returns
        -------
        Union[Response, NoneType]
        """

        try:
            log_api("=> frame.wait_for_navigation started")
            result = mapping.from_impl_nullable(
                self._sync(
                    self._impl_obj.wait_for_navigation(
                        url=self._wrap_handler(url),
                        waitUntil=wait_until,
                        timeout=timeout,
                    )
                )
            )
            log_api("<= frame.wait_for_navigation succeded")
            return result
        except Exception as e:
            log_api("<= frame.wait_for_navigation failed")
            raise e

    def wait_for_load_state(
        self,
        state: Literal["domcontentloaded", "load", "networkidle"] = None,
        timeout: float = None,
    ) -> NoneType:
        """Frame.wait_for_load_state

        Waits for the required load state to be reached.

        This returns when the frame reaches a required load state, `load` by default. The navigation must have been committed
        when this method is called. If current document has already reached the required state, resolves immediately.

        Parameters
        ----------
        state : Union["domcontentloaded", "load", "networkidle", NoneType]
            Optional load state to wait for, defaults to `load`. If the state has been already reached while loading current
            document, the method returns immediately. Can be one of:
            - `'load'` - wait for the `load` event to be fired.
            - `'domcontentloaded'` - wait for the `DOMContentLoaded` event to be fired.
            - `'networkidle'` - wait until there are no network connections for at least `500` ms.
        timeout : Union[float, NoneType]
            Maximum operation time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be
            changed by using the `browser_context.set_default_navigation_timeout()`,
            `browser_context.set_default_timeout()`, `page.set_default_navigation_timeout()` or
            `page.set_default_timeout()` methods.
        """

        try:
            log_api("=> frame.wait_for_load_state started")
            result = mapping.from_maybe_impl(
                self._sync(
                    self._impl_obj.wait_for_load_state(state=state, timeout=timeout)
                )
            )
            log_api("<= frame.wait_for_load_state succeded")
            return result
        except Exception as e:
            log_api("<= frame.wait_for_load_state failed")
            raise e

    def frame_element(self) -> "ElementHandle":
        """Frame.frame_element

        Returns the `frame` or `iframe` element handle which corresponds to this frame.

        This is an inverse of `element_handle.content_frame()`. Note that returned handle actually belongs to the parent
        frame.

        This method throws an error if the frame has been detached before `frameElement()` returns.

        Returns
        -------
        ElementHandle
        """

        try:
            log_api("=> frame.frame_element started")
            result = mapping.from_impl(self._sync(self._impl_obj.frame_element()))
            log_api("<= frame.frame_element succeded")
            return result
        except Exception as e:
            log_api("<= frame.frame_element failed")
            raise e

    def evaluate(
        self, expression: str, arg: typing.Any = None, force_expr: bool = None
    ) -> typing.Any:
        """Frame.evaluate

        Returns the return value of `pageFunction`

        If the function passed to the `frame.evaluate` returns a [Promise], then `frame.evaluate` would wait for the promise to
        resolve and return its value.

        If the function passed to the `frame.evaluate` returns a non-[Serializable] value, then `frame.evaluate` returns
        `undefined`. DevTools Protocol also supports transferring some additional values that are not serializable by `JSON`:
        `-0`, `NaN`, `Infinity`, `-Infinity`, and bigint literals.

        A string can also be passed in instead of a function.

        `ElementHandle` instances can be passed as an argument to the `frame.evaluate`:

        Parameters
        ----------
        expression : str
            Function to be evaluated in browser context
        force_expr : bool
            Whether to treat given expression as JavaScript evaluate expression, even though it looks like an arrow function
        arg : Union[Any, NoneType]
            Optional argument to pass to `pageFunction`

        Returns
        -------
        Any
        """

        try:
            log_api("=> frame.evaluate started")
            result = mapping.from_maybe_impl(
                self._sync(
                    self._impl_obj.evaluate(
                        expression=expression,
                        arg=mapping.to_impl(arg),
                        force_expr=force_expr,
                    )
                )
            )
            log_api("<= frame.evaluate succeded")
            return result
        except Exception as e:
            log_api("<= frame.evaluate failed")
            raise e

    def evaluate_handle(
        self, expression: str, arg: typing.Any = None, force_expr: bool = None
    ) -> "JSHandle":
        """Frame.evaluate_handle

        Returns the return value of `pageFunction` as in-page object (JSHandle).

        The only difference between `frame.evaluate` and `frame.evaluateHandle` is that `frame.evaluateHandle` returns in-page
        object (JSHandle).

        If the function, passed to the `frame.evaluateHandle`, returns a [Promise], then `frame.evaluateHandle` would wait for
        the promise to resolve and return its value.

        A string can also be passed in instead of a function.

        `JSHandle` instances can be passed as an argument to the `frame.evaluateHandle`:

        Parameters
        ----------
        expression : str
            Function to be evaluated in the page context
        force_expr : bool
            Whether to treat given expression as JavaScript evaluate expression, even though it looks like an arrow function
        arg : Union[Any, NoneType]
            Optional argument to pass to `pageFunction`

        Returns
        -------
        JSHandle
        """

        try:
            log_api("=> frame.evaluate_handle started")
            result = mapping.from_impl(
                self._sync(
                    self._impl_obj.evaluate_handle(
                        expression=expression,
                        arg=mapping.to_impl(arg),
                        force_expr=force_expr,
                    )
                )
            )
            log_api("<= frame.evaluate_handle succeded")
            return result
        except Exception as e:
            log_api("<= frame.evaluate_handle failed")
            raise e

    def query_selector(self, selector: str) -> typing.Union["ElementHandle", NoneType]:
        """Frame.query_selector

        Returns the ElementHandle pointing to the frame element.

        The method finds an element matching the specified selector within the frame. See
        [Working with selectors](./selectors.md#working-with-selectors) for more details. If no elements match the selector,
        returns `null`.

        Parameters
        ----------
        selector : str
            A selector to query for. See [working with selectors](./selectors.md#working-with-selectors) for more details.

        Returns
        -------
        Union[ElementHandle, NoneType]
        """

        try:
            log_api("=> frame.query_selector started")
            result = mapping.from_impl_nullable(
                self._sync(self._impl_obj.query_selector(selector=selector))
            )
            log_api("<= frame.query_selector succeded")
            return result
        except Exception as e:
            log_api("<= frame.query_selector failed")
            raise e

    def query_selector_all(self, selector: str) -> typing.List["ElementHandle"]:
        """Frame.query_selector_all

        Returns the ElementHandles pointing to the frame elements.

        The method finds all elements matching the specified selector within the frame. See
        [Working with selectors](./selectors.md#working-with-selectors) for more details. If no elements match the selector,
        returns empty array.

        Parameters
        ----------
        selector : str
            A selector to query for. See [working with selectors](./selectors.md#working-with-selectors) for more details.

        Returns
        -------
        List[ElementHandle]
        """

        try:
            log_api("=> frame.query_selector_all started")
            result = mapping.from_impl_list(
                self._sync(self._impl_obj.query_selector_all(selector=selector))
            )
            log_api("<= frame.query_selector_all succeded")
            return result
        except Exception as e:
            log_api("<= frame.query_selector_all failed")
            raise e

    def wait_for_selector(
        self,
        selector: str,
        timeout: float = None,
        state: Literal["attached", "detached", "hidden", "visible"] = None,
    ) -> typing.Union["ElementHandle", NoneType]:
        """Frame.wait_for_selector

        Returns when element specified by selector satisfies `state` option. Returns `null` if waiting for `hidden` or
        `detached`.

        Wait for the `selector` to satisfy `state` option (either appear/disappear from dom, or become visible/hidden). If at
        the moment of calling the method `selector` already satisfies the condition, the method will return immediately. If the
        selector doesn't satisfy the condition for the `timeout` milliseconds, the function will throw.

        This method works across navigations:

        Parameters
        ----------
        selector : str
            A selector to query for. See [working with selectors](./selectors.md#working-with-selectors) for more details.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        state : Union["attached", "detached", "hidden", "visible", NoneType]
            Defaults to `'visible'`. Can be either:
            - `'attached'` - wait for element to be present in DOM.
            - `'detached'` - wait for element to not be present in DOM.
            - `'visible'` - wait for element to have non-empty bounding box and no `visibility:hidden`. Note that element without
              any content or with `display:none` has an empty bounding box and is not considered visible.
            - `'hidden'` - wait for element to be either detached from DOM, or have an empty bounding box or `visibility:hidden`.
              This is opposite to the `'visible'` option.

        Returns
        -------
        Union[ElementHandle, NoneType]
        """

        try:
            log_api("=> frame.wait_for_selector started")
            result = mapping.from_impl_nullable(
                self._sync(
                    self._impl_obj.wait_for_selector(
                        selector=selector, timeout=timeout, state=state
                    )
                )
            )
            log_api("<= frame.wait_for_selector succeded")
            return result
        except Exception as e:
            log_api("<= frame.wait_for_selector failed")
            raise e

    def dispatch_event(
        self,
        selector: str,
        type: str,
        event_init: typing.Dict = None,
        timeout: float = None,
    ) -> NoneType:
        """Frame.dispatch_event

        The snippet below dispatches the `click` event on the element. Regardless of the visibility state of the elment, `click`
        is dispatched. This is equivalend to calling
        [element.click()](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/click).

        Under the hood, it creates an instance of an event based on the given `type`, initializes it with `eventInit` properties
        and dispatches it on the element. Events are `composed`, `cancelable` and bubble by default.

        Since `eventInit` is event-specific, please refer to the events documentation for the lists of initial properties:
        - [DragEvent](https://developer.mozilla.org/en-US/docs/Web/API/DragEvent/DragEvent)
        - [FocusEvent](https://developer.mozilla.org/en-US/docs/Web/API/FocusEvent/FocusEvent)
        - [KeyboardEvent](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/KeyboardEvent)
        - [MouseEvent](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/MouseEvent)
        - [PointerEvent](https://developer.mozilla.org/en-US/docs/Web/API/PointerEvent/PointerEvent)
        - [TouchEvent](https://developer.mozilla.org/en-US/docs/Web/API/TouchEvent/TouchEvent)
        - [Event](https://developer.mozilla.org/en-US/docs/Web/API/Event/Event)

        You can also specify `JSHandle` as the property value if you want live objects to be passed into the event:

        Parameters
        ----------
        selector : str
            A selector to search for element. If there are multiple elements satisfying the selector, the first will be used. See
            [working with selectors](./selectors.md#working-with-selectors) for more details.
        type : str
            DOM event type: `"click"`, `"dragstart"`, etc.
        event_init : Union[Dict, NoneType]
            Optional event-specific initialization properties.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        """

        try:
            log_api("=> frame.dispatch_event started")
            result = mapping.from_maybe_impl(
                self._sync(
                    self._impl_obj.dispatch_event(
                        selector=selector,
                        type=type,
                        eventInit=mapping.to_impl(event_init),
                        timeout=timeout,
                    )
                )
            )
            log_api("<= frame.dispatch_event succeded")
            return result
        except Exception as e:
            log_api("<= frame.dispatch_event failed")
            raise e

    def eval_on_selector(
        self,
        selector: str,
        expression: str,
        arg: typing.Any = None,
        force_expr: bool = None,
    ) -> typing.Any:
        """Frame.eval_on_selector

        Returns the return value of `pageFunction`

        The method finds an element matching the specified selector within the frame and passes it as a first argument to
        `pageFunction`. See [Working with selectors](./selectors.md#working-with-selectors) for more details. If no elements
        match the selector, the method throws an error.

        If `pageFunction` returns a [Promise], then `frame.$eval` would wait for the promise to resolve and return its value.

        Examples:

        Parameters
        ----------
        selector : str
            A selector to query for. See [working with selectors](./selectors.md#working-with-selectors) for more details.
        expression : str
            Function to be evaluated in browser context
        force_expr : bool
            Whether to treat given expression as JavaScript evaluate expression, even though it looks like an arrow function
        arg : Union[Any, NoneType]
            Optional argument to pass to `pageFunction`

        Returns
        -------
        Any
        """

        try:
            log_api("=> frame.eval_on_selector started")
            result = mapping.from_maybe_impl(
                self._sync(
                    self._impl_obj.eval_on_selector(
                        selector=selector,
                        expression=expression,
                        arg=mapping.to_impl(arg),
                        force_expr=force_expr,
                    )
                )
            )
            log_api("<= frame.eval_on_selector succeded")
            return result
        except Exception as e:
            log_api("<= frame.eval_on_selector failed")
            raise e

    def eval_on_selector_all(
        self,
        selector: str,
        expression: str,
        arg: typing.Any = None,
        force_expr: bool = None,
    ) -> typing.Any:
        """Frame.eval_on_selector_all

        Returns the return value of `pageFunction`

        The method finds all elements matching the specified selector within the frame and passes an array of matched elements
        as a first argument to `pageFunction`. See [Working with selectors](./selectors.md#working-with-selectors) for more
        details.

        If `pageFunction` returns a [Promise], then `frame.$$eval` would wait for the promise to resolve and return its value.

        Examples:

        Parameters
        ----------
        selector : str
            A selector to query for. See [working with selectors](./selectors.md#working-with-selectors) for more details.
        expression : str
            Function to be evaluated in browser context
        force_expr : bool
            Whether to treat given expression as JavaScript evaluate expression, even though it looks like an arrow function
        arg : Union[Any, NoneType]
            Optional argument to pass to `pageFunction`

        Returns
        -------
        Any
        """

        try:
            log_api("=> frame.eval_on_selector_all started")
            result = mapping.from_maybe_impl(
                self._sync(
                    self._impl_obj.eval_on_selector_all(
                        selector=selector,
                        expression=expression,
                        arg=mapping.to_impl(arg),
                        force_expr=force_expr,
                    )
                )
            )
            log_api("<= frame.eval_on_selector_all succeded")
            return result
        except Exception as e:
            log_api("<= frame.eval_on_selector_all failed")
            raise e

    def content(self) -> str:
        """Frame.content

        Gets the full HTML contents of the frame, including the doctype.

        Returns
        -------
        str
        """

        try:
            log_api("=> frame.content started")
            result = mapping.from_maybe_impl(self._sync(self._impl_obj.content()))
            log_api("<= frame.content succeded")
            return result
        except Exception as e:
            log_api("<= frame.content failed")
            raise e

    def set_content(
        self,
        html: str,
        timeout: float = None,
        wait_until: Literal["domcontentloaded", "load", "networkidle"] = None,
    ) -> NoneType:
        """Frame.set_content

        Parameters
        ----------
        html : str
            HTML markup to assign to the page.
        timeout : Union[float, NoneType]
            Maximum operation time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be
            changed by using the `browser_context.set_default_navigation_timeout()`,
            `browser_context.set_default_timeout()`, `page.set_default_navigation_timeout()` or
            `page.set_default_timeout()` methods.
        wait_until : Union["domcontentloaded", "load", "networkidle", NoneType]
            When to consider operation succeeded, defaults to `load`. Events can be either:
            - `'domcontentloaded'` - consider operation to be finished when the `DOMContentLoaded` event is fired.
            - `'load'` - consider operation to be finished when the `load` event is fired.
            - `'networkidle'` - consider operation to be finished when there are no network connections for at least `500` ms.
        """

        try:
            log_api("=> frame.set_content started")
            result = mapping.from_maybe_impl(
                self._sync(
                    self._impl_obj.set_content(
                        html=html, timeout=timeout, waitUntil=wait_until
                    )
                )
            )
            log_api("<= frame.set_content succeded")
            return result
        except Exception as e:
            log_api("<= frame.set_content failed")
            raise e

    def is_detached(self) -> bool:
        """Frame.is_detached

        Returns `true` if the frame has been detached, or `false` otherwise.

        Returns
        -------
        bool
        """

        try:
            log_api("=> frame.is_detached started")
            result = mapping.from_maybe_impl(self._impl_obj.is_detached())
            log_api("<= frame.is_detached succeded")
            return result
        except Exception as e:
            log_api("<= frame.is_detached failed")
            raise e

    def add_script_tag(
        self,
        url: str = None,
        path: typing.Union[str, pathlib.Path] = None,
        content: str = None,
        type: str = None,
    ) -> "ElementHandle":
        """Frame.add_script_tag

        Returns the added tag when the script's onload fires or when the script content was injected into frame.

        Adds a `<script>` tag into the page with the desired url or content.

        Parameters
        ----------
        url : Union[str, NoneType]
            URL of a script to be added. Optional.
        path : Union[pathlib.Path, str, NoneType]
            Path to the JavaScript file to be injected into frame. If `path` is a relative path, then it is resolved relative to the
            current working directory. Optional.
        content : Union[str, NoneType]
            Raw JavaScript content to be injected into frame. Optional.
        type : Union[str, NoneType]
            Script type. Use 'module' in order to load a Javascript ES6 module. See
            [script](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/script) for more details. Optional.

        Returns
        -------
        ElementHandle
        """

        try:
            log_api("=> frame.add_script_tag started")
            result = mapping.from_impl(
                self._sync(
                    self._impl_obj.add_script_tag(
                        url=url, path=path, content=content, type=type
                    )
                )
            )
            log_api("<= frame.add_script_tag succeded")
            return result
        except Exception as e:
            log_api("<= frame.add_script_tag failed")
            raise e

    def add_style_tag(
        self,
        url: str = None,
        path: typing.Union[str, pathlib.Path] = None,
        content: str = None,
    ) -> "ElementHandle":
        """Frame.add_style_tag

        Returns the added tag when the stylesheet's onload fires or when the CSS content was injected into frame.

        Adds a `<link rel="stylesheet">` tag into the page with the desired url or a `<style type="text/css">` tag with the
        content.

        Parameters
        ----------
        url : Union[str, NoneType]
            URL of the `<link>` tag. Optional.
        path : Union[pathlib.Path, str, NoneType]
            Path to the CSS file to be injected into frame. If `path` is a relative path, then it is resolved relative to the
            current working directory. Optional.
        content : Union[str, NoneType]
            Raw CSS content to be injected into frame. Optional.

        Returns
        -------
        ElementHandle
        """

        try:
            log_api("=> frame.add_style_tag started")
            result = mapping.from_impl(
                self._sync(
                    self._impl_obj.add_style_tag(url=url, path=path, content=content)
                )
            )
            log_api("<= frame.add_style_tag succeded")
            return result
        except Exception as e:
            log_api("<= frame.add_style_tag failed")
            raise e

    def click(
        self,
        selector: str,
        modifiers: typing.Union[
            typing.List[Literal["Alt", "Control", "Meta", "Shift"]]
        ] = None,
        position: typing.Union[typing.Tuple[float, float]] = None,
        delay: float = None,
        button: Literal["left", "middle", "right"] = None,
        click_count: int = None,
        timeout: float = None,
        force: bool = None,
        no_wait_after: bool = None,
    ) -> NoneType:
        """Frame.click

        This method clicks an element matching `selector` by performing the following steps:
        1. Find an element match matching `selector`. If there is none, wait until a matching element is attached to the DOM.
        1. Wait for [actionability](./actionability.md) checks on the matched element, unless `force` option is set. If the
           element is detached during the checks, the whole action is retried.
        1. Scroll the element into view if needed.
        1. Use `page.mouse` to click in the center of the element, or the specified `position`.
        1. Wait for initiated navigations to either succeed or fail, unless `noWaitAfter` option is set.

        When all steps combined have not finished during the specified `timeout`, this method rejects with a `TimeoutError`.
        Passing zero timeout disables this.

        Parameters
        ----------
        selector : str
            A selector to search for element. If there are multiple elements satisfying the selector, the first will be used. See
            [working with selectors](./selectors.md#working-with-selectors) for more details.
        modifiers : Union[List[Union["Alt", "Control", "Meta", "Shift"]], NoneType]
            Modifier keys to press. Ensures that only these modifiers are pressed during the operation, and then restores current
            modifiers back. If not specified, currently pressed modifiers are used.
        position : Union[typing.Tuple[float, float], NoneType]
            A point to use relative to the top-left corner of element padding box. If not specified, uses some visible point of the
            element.
        delay : Union[float, NoneType]
            Time to wait between `mousedown` and `mouseup` in milliseconds. Defaults to 0.
        button : Union["left", "middle", "right", NoneType]
            Defaults to `left`.
        click_count : Union[int, NoneType]
            defaults to 1. See [UIEvent.detail].
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        force : Union[bool, NoneType]
            Whether to bypass the [actionability](./actionability.md) checks. Defaults to `false`.
        no_wait_after : Union[bool, NoneType]
            Actions that initiate navigations are waiting for these navigations to happen and for pages to start loading. You can
            opt out of waiting via setting this flag. You would only need this option in the exceptional cases such as navigating to
            inaccessible pages. Defaults to `false`.
        """

        try:
            log_api("=> frame.click started")
            result = mapping.from_maybe_impl(
                self._sync(
                    self._impl_obj.click(
                        selector=selector,
                        modifiers=modifiers,
                        position=position,
                        delay=delay,
                        button=button,
                        clickCount=click_count,
                        timeout=timeout,
                        force=force,
                        noWaitAfter=no_wait_after,
                    )
                )
            )
            log_api("<= frame.click succeded")
            return result
        except Exception as e:
            log_api("<= frame.click failed")
            raise e

    def dblclick(
        self,
        selector: str,
        modifiers: typing.Union[
            typing.List[Literal["Alt", "Control", "Meta", "Shift"]]
        ] = None,
        position: typing.Union[typing.Tuple[float, float]] = None,
        delay: float = None,
        button: Literal["left", "middle", "right"] = None,
        timeout: float = None,
        force: bool = None,
        no_wait_after: bool = None,
    ) -> NoneType:
        """Frame.dblclick

        This method double clicks an element matching `selector` by performing the following steps:
        1. Find an element match matching `selector`. If there is none, wait until a matching element is attached to the DOM.
        1. Wait for [actionability](./actionability.md) checks on the matched element, unless `force` option is set. If the
           element is detached during the checks, the whole action is retried.
        1. Scroll the element into view if needed.
        1. Use `page.mouse` to double click in the center of the element, or the specified `position`.
        1. Wait for initiated navigations to either succeed or fail, unless `noWaitAfter` option is set. Note that if the
           first click of the `dblclick()` triggers a navigation event, this method will reject.

        When all steps combined have not finished during the specified `timeout`, this method rejects with a `TimeoutError`.
        Passing zero timeout disables this.

        > **NOTE** `frame.dblclick()` dispatches two `click` events and a single `dblclick` event.

        Parameters
        ----------
        selector : str
            A selector to search for element. If there are multiple elements satisfying the selector, the first will be used. See
            [working with selectors](./selectors.md#working-with-selectors) for more details.
        modifiers : Union[List[Union["Alt", "Control", "Meta", "Shift"]], NoneType]
            Modifier keys to press. Ensures that only these modifiers are pressed during the operation, and then restores current
            modifiers back. If not specified, currently pressed modifiers are used.
        position : Union[typing.Tuple[float, float], NoneType]
            A point to use relative to the top-left corner of element padding box. If not specified, uses some visible point of the
            element.
        delay : Union[float, NoneType]
            Time to wait between `mousedown` and `mouseup` in milliseconds. Defaults to 0.
        button : Union["left", "middle", "right", NoneType]
            Defaults to `left`.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        force : Union[bool, NoneType]
            Whether to bypass the [actionability](./actionability.md) checks. Defaults to `false`.
        no_wait_after : Union[bool, NoneType]
            Actions that initiate navigations are waiting for these navigations to happen and for pages to start loading. You can
            opt out of waiting via setting this flag. You would only need this option in the exceptional cases such as navigating to
            inaccessible pages. Defaults to `false`.
        """

        try:
            log_api("=> frame.dblclick started")
            result = mapping.from_maybe_impl(
                self._sync(
                    self._impl_obj.dblclick(
                        selector=selector,
                        modifiers=modifiers,
                        position=position,
                        delay=delay,
                        button=button,
                        timeout=timeout,
                        force=force,
                        noWaitAfter=no_wait_after,
                    )
                )
            )
            log_api("<= frame.dblclick succeded")
            return result
        except Exception as e:
            log_api("<= frame.dblclick failed")
            raise e

    def tap(
        self,
        selector: str,
        modifiers: typing.Union[
            typing.List[Literal["Alt", "Control", "Meta", "Shift"]]
        ] = None,
        position: typing.Union[typing.Tuple[float, float]] = None,
        timeout: float = None,
        force: bool = None,
        no_wait_after: bool = None,
    ) -> NoneType:
        """Frame.tap

        This method taps an element matching `selector` by performing the following steps:
        1. Find an element match matching `selector`. If there is none, wait until a matching element is attached to the DOM.
        1. Wait for [actionability](./actionability.md) checks on the matched element, unless `force` option is set. If the
           element is detached during the checks, the whole action is retried.
        1. Scroll the element into view if needed.
        1. Use `page.touchscreen` to tap the center of the element, or the specified `position`.
        1. Wait for initiated navigations to either succeed or fail, unless `noWaitAfter` option is set.

        When all steps combined have not finished during the specified `timeout`, this method rejects with a `TimeoutError`.
        Passing zero timeout disables this.

        > **NOTE** `frame.tap()` requires that the `hasTouch` option of the browser context be set to true.

        Parameters
        ----------
        selector : str
            A selector to search for element. If there are multiple elements satisfying the selector, the first will be used. See
            [working with selectors](./selectors.md#working-with-selectors) for more details.
        modifiers : Union[List[Union["Alt", "Control", "Meta", "Shift"]], NoneType]
            Modifier keys to press. Ensures that only these modifiers are pressed during the operation, and then restores current
            modifiers back. If not specified, currently pressed modifiers are used.
        position : Union[typing.Tuple[float, float], NoneType]
            A point to use relative to the top-left corner of element padding box. If not specified, uses some visible point of the
            element.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        force : Union[bool, NoneType]
            Whether to bypass the [actionability](./actionability.md) checks. Defaults to `false`.
        no_wait_after : Union[bool, NoneType]
            Actions that initiate navigations are waiting for these navigations to happen and for pages to start loading. You can
            opt out of waiting via setting this flag. You would only need this option in the exceptional cases such as navigating to
            inaccessible pages. Defaults to `false`.
        """

        try:
            log_api("=> frame.tap started")
            result = mapping.from_maybe_impl(
                self._sync(
                    self._impl_obj.tap(
                        selector=selector,
                        modifiers=modifiers,
                        position=position,
                        timeout=timeout,
                        force=force,
                        noWaitAfter=no_wait_after,
                    )
                )
            )
            log_api("<= frame.tap succeded")
            return result
        except Exception as e:
            log_api("<= frame.tap failed")
            raise e

    def fill(
        self,
        selector: str,
        value: str,
        timeout: float = None,
        no_wait_after: bool = None,
    ) -> NoneType:
        """Frame.fill

        This method waits for an element matching `selector`, waits for [actionability](./actionability.md) checks, focuses the
        element, fills it and triggers an `input` event after filling. If the element matching `selector` is not an `<input>`,
        `<textarea>` or `[contenteditable]` element, this method throws an error. Note that you can pass an empty string to
        clear the input field.

        To send fine-grained keyboard events, use `frame.type()`.

        Parameters
        ----------
        selector : str
            A selector to search for element. If there are multiple elements satisfying the selector, the first will be used. See
            [working with selectors](./selectors.md#working-with-selectors) for more details.
        value : str
            Value to fill for the `<input>`, `<textarea>` or `[contenteditable]` element.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        no_wait_after : Union[bool, NoneType]
            Actions that initiate navigations are waiting for these navigations to happen and for pages to start loading. You can
            opt out of waiting via setting this flag. You would only need this option in the exceptional cases such as navigating to
            inaccessible pages. Defaults to `false`.
        """

        try:
            log_api("=> frame.fill started")
            result = mapping.from_maybe_impl(
                self._sync(
                    self._impl_obj.fill(
                        selector=selector,
                        value=value,
                        timeout=timeout,
                        noWaitAfter=no_wait_after,
                    )
                )
            )
            log_api("<= frame.fill succeded")
            return result
        except Exception as e:
            log_api("<= frame.fill failed")
            raise e

    def focus(self, selector: str, timeout: float = None) -> NoneType:
        """Frame.focus

        This method fetches an element with `selector` and focuses it. If there's no element matching `selector`, the method
        waits until a matching element appears in the DOM.

        Parameters
        ----------
        selector : str
            A selector to search for element. If there are multiple elements satisfying the selector, the first will be used. See
            [working with selectors](./selectors.md#working-with-selectors) for more details.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        """

        try:
            log_api("=> frame.focus started")
            result = mapping.from_maybe_impl(
                self._sync(self._impl_obj.focus(selector=selector, timeout=timeout))
            )
            log_api("<= frame.focus succeded")
            return result
        except Exception as e:
            log_api("<= frame.focus failed")
            raise e

    def text_content(
        self, selector: str, timeout: float = None
    ) -> typing.Union[str, NoneType]:
        """Frame.text_content

        Returns `element.textContent`.

        Parameters
        ----------
        selector : str
            A selector to search for element. If there are multiple elements satisfying the selector, the first will be used. See
            [working with selectors](./selectors.md#working-with-selectors) for more details.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.

        Returns
        -------
        Union[str, NoneType]
        """

        try:
            log_api("=> frame.text_content started")
            result = mapping.from_maybe_impl(
                self._sync(
                    self._impl_obj.text_content(selector=selector, timeout=timeout)
                )
            )
            log_api("<= frame.text_content succeded")
            return result
        except Exception as e:
            log_api("<= frame.text_content failed")
            raise e

    def inner_text(self, selector: str, timeout: float = None) -> str:
        """Frame.inner_text

        Returns `element.innerText`.

        Parameters
        ----------
        selector : str
            A selector to search for element. If there are multiple elements satisfying the selector, the first will be used. See
            [working with selectors](./selectors.md#working-with-selectors) for more details.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.

        Returns
        -------
        str
        """

        try:
            log_api("=> frame.inner_text started")
            result = mapping.from_maybe_impl(
                self._sync(
                    self._impl_obj.inner_text(selector=selector, timeout=timeout)
                )
            )
            log_api("<= frame.inner_text succeded")
            return result
        except Exception as e:
            log_api("<= frame.inner_text failed")
            raise e

    def inner_html(self, selector: str, timeout: float = None) -> str:
        """Frame.inner_html

        Returns `element.innerHTML`.

        Parameters
        ----------
        selector : str
            A selector to search for element. If there are multiple elements satisfying the selector, the first will be used. See
            [working with selectors](./selectors.md#working-with-selectors) for more details.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.

        Returns
        -------
        str
        """

        try:
            log_api("=> frame.inner_html started")
            result = mapping.from_maybe_impl(
                self._sync(
                    self._impl_obj.inner_html(selector=selector, timeout=timeout)
                )
            )
            log_api("<= frame.inner_html succeded")
            return result
        except Exception as e:
            log_api("<= frame.inner_html failed")
            raise e

    def get_attribute(
        self, selector: str, name: str, timeout: float = None
    ) -> typing.Union[str, NoneType]:
        """Frame.get_attribute

        Returns element attribute value.

        Parameters
        ----------
        selector : str
            A selector to search for element. If there are multiple elements satisfying the selector, the first will be used. See
            [working with selectors](./selectors.md#working-with-selectors) for more details.
        name : str
            Attribute name to get the value for.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.

        Returns
        -------
        Union[str, NoneType]
        """

        try:
            log_api("=> frame.get_attribute started")
            result = mapping.from_maybe_impl(
                self._sync(
                    self._impl_obj.get_attribute(
                        selector=selector, name=name, timeout=timeout
                    )
                )
            )
            log_api("<= frame.get_attribute succeded")
            return result
        except Exception as e:
            log_api("<= frame.get_attribute failed")
            raise e

    def hover(
        self,
        selector: str,
        modifiers: typing.Union[
            typing.List[Literal["Alt", "Control", "Meta", "Shift"]]
        ] = None,
        position: typing.Union[typing.Tuple[float, float]] = None,
        timeout: float = None,
        force: bool = None,
    ) -> NoneType:
        """Frame.hover

        This method hovers over an element matching `selector` by performing the following steps:
        1. Find an element match matching `selector`. If there is none, wait until a matching element is attached to the DOM.
        1. Wait for [actionability](./actionability.md) checks on the matched element, unless `force` option is set. If the
           element is detached during the checks, the whole action is retried.
        1. Scroll the element into view if needed.
        1. Use `page.mouse` to hover over the center of the element, or the specified `position`.
        1. Wait for initiated navigations to either succeed or fail, unless `noWaitAfter` option is set.

        When all steps combined have not finished during the specified `timeout`, this method rejects with a `TimeoutError`.
        Passing zero timeout disables this.

        Parameters
        ----------
        selector : str
            A selector to search for element. If there are multiple elements satisfying the selector, the first will be used. See
            [working with selectors](./selectors.md#working-with-selectors) for more details.
        modifiers : Union[List[Union["Alt", "Control", "Meta", "Shift"]], NoneType]
            Modifier keys to press. Ensures that only these modifiers are pressed during the operation, and then restores current
            modifiers back. If not specified, currently pressed modifiers are used.
        position : Union[typing.Tuple[float, float], NoneType]
            A point to use relative to the top-left corner of element padding box. If not specified, uses some visible point of the
            element.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        force : Union[bool, NoneType]
            Whether to bypass the [actionability](./actionability.md) checks. Defaults to `false`.
        """

        try:
            log_api("=> frame.hover started")
            result = mapping.from_maybe_impl(
                self._sync(
                    self._impl_obj.hover(
                        selector=selector,
                        modifiers=modifiers,
                        position=position,
                        timeout=timeout,
                        force=force,
                    )
                )
            )
            log_api("<= frame.hover succeded")
            return result
        except Exception as e:
            log_api("<= frame.hover failed")
            raise e

    def select_option(
        self,
        selector: str,
        value: typing.Union[str, typing.List[str]] = None,
        index: typing.Union[int, typing.List[int]] = None,
        label: typing.Union[str, typing.List[str]] = None,
        element: typing.Union["ElementHandle", typing.List["ElementHandle"]] = None,
        timeout: float = None,
        no_wait_after: bool = None,
    ) -> typing.List[str]:
        """Frame.select_option

        Returns the array of option values that have been successfully selected.

        Triggers a `change` and `input` event once all the provided options have been selected. If there's no `<select>` element
        matching `selector`, the method throws an error.

        Parameters
        ----------
        selector : str
            A selector to query for. See [working with selectors](./selectors.md#working-with-selectors) for more details.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        no_wait_after : Union[bool, NoneType]
            Actions that initiate navigations are waiting for these navigations to happen and for pages to start loading. You can
            opt out of waiting via setting this flag. You would only need this option in the exceptional cases such as navigating to
            inaccessible pages. Defaults to `false`.

        Returns
        -------
        List[str]
        """

        try:
            log_api("=> frame.select_option started")
            result = mapping.from_maybe_impl(
                self._sync(
                    self._impl_obj.select_option(
                        selector=selector,
                        value=value,
                        index=index,
                        label=label,
                        element=mapping.to_impl(element),
                        timeout=timeout,
                        noWaitAfter=no_wait_after,
                    )
                )
            )
            log_api("<= frame.select_option succeded")
            return result
        except Exception as e:
            log_api("<= frame.select_option failed")
            raise e

    def set_input_files(
        self,
        selector: str,
        files: typing.Union[
            str,
            pathlib.Path,
            "FilePayload",
            typing.List[str],
            typing.List[pathlib.Path],
            typing.List["FilePayload"],
        ],
        timeout: float = None,
        no_wait_after: bool = None,
    ) -> NoneType:
        """Frame.set_input_files

        This method expects `selector` to point to an
        [input element](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input).

        Sets the value of the file input to these file paths or files. If some of the `filePaths` are relative paths, then they
        are resolved relative to the the current working directory. For empty array, clears the selected files.

        Parameters
        ----------
        selector : str
            A selector to search for element. If there are multiple elements satisfying the selector, the first will be used. See
            [working with selectors](./selectors.md#working-with-selectors) for more details.
        files : Union[List[pathlib.Path], List[str], List[{name: str, mime_type: str, buffer: bytes}], pathlib.Path, str, {name: str, mime_type: str, buffer: bytes}]
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        no_wait_after : Union[bool, NoneType]
            Actions that initiate navigations are waiting for these navigations to happen and for pages to start loading. You can
            opt out of waiting via setting this flag. You would only need this option in the exceptional cases such as navigating to
            inaccessible pages. Defaults to `false`.
        """

        try:
            log_api("=> frame.set_input_files started")
            result = mapping.from_maybe_impl(
                self._sync(
                    self._impl_obj.set_input_files(
                        selector=selector,
                        files=files,
                        timeout=timeout,
                        noWaitAfter=no_wait_after,
                    )
                )
            )
            log_api("<= frame.set_input_files succeded")
            return result
        except Exception as e:
            log_api("<= frame.set_input_files failed")
            raise e

    def type(
        self,
        selector: str,
        text: str,
        delay: float = None,
        timeout: float = None,
        no_wait_after: bool = None,
    ) -> NoneType:
        """Frame.type

        Sends a `keydown`, `keypress`/`input`, and `keyup` event for each character in the text. `frame.type` can be used to
        send fine-grained keyboard events. To fill values in form fields, use `frame.fill()`.

        To press a special key, like `Control` or `ArrowDown`, use `keyboard.press()`.

        Parameters
        ----------
        selector : str
            A selector to search for element. If there are multiple elements satisfying the selector, the first will be used. See
            [working with selectors](./selectors.md#working-with-selectors) for more details.
        text : str
            A text to type into a focused element.
        delay : Union[float, NoneType]
            Time to wait between key presses in milliseconds. Defaults to 0.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        no_wait_after : Union[bool, NoneType]
            Actions that initiate navigations are waiting for these navigations to happen and for pages to start loading. You can
            opt out of waiting via setting this flag. You would only need this option in the exceptional cases such as navigating to
            inaccessible pages. Defaults to `false`.
        """

        try:
            log_api("=> frame.type started")
            result = mapping.from_maybe_impl(
                self._sync(
                    self._impl_obj.type(
                        selector=selector,
                        text=text,
                        delay=delay,
                        timeout=timeout,
                        noWaitAfter=no_wait_after,
                    )
                )
            )
            log_api("<= frame.type succeded")
            return result
        except Exception as e:
            log_api("<= frame.type failed")
            raise e

    def press(
        self,
        selector: str,
        key: str,
        delay: float = None,
        timeout: float = None,
        no_wait_after: bool = None,
    ) -> NoneType:
        """Frame.press

        `key` can specify the intended [keyboardEvent.key](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/key)
        value or a single character to generate the text for. A superset of the `key` values can be found
        [here](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/key/Key_Values). Examples of the keys are:

        `F1` - `F12`, `Digit0`- `Digit9`, `KeyA`- `KeyZ`, `Backquote`, `Minus`, `Equal`, `Backslash`, `Backspace`, `Tab`,
        `Delete`, `Escape`, `ArrowDown`, `End`, `Enter`, `Home`, `Insert`, `PageDown`, `PageUp`, `ArrowRight`, `ArrowUp`, etc.

        Following modification shortcuts are also supported: `Shift`, `Control`, `Alt`, `Meta`, `ShiftLeft`.

        Holding down `Shift` will type the text that corresponds to the `key` in the upper case.

        If `key` is a single character, it is case-sensitive, so the values `a` and `A` will generate different respective
        texts.

        Shortcuts such as `key: "Control+o"` or `key: "Control+Shift+T"` are supported as well. When speficied with the
        modifier, modifier is pressed and being held while the subsequent key is being pressed.

        Parameters
        ----------
        selector : str
            A selector to search for element. If there are multiple elements satisfying the selector, the first will be used. See
            [working with selectors](./selectors.md#working-with-selectors) for more details.
        key : str
            Name of the key to press or a character to generate, such as `ArrowLeft` or `a`.
        delay : Union[float, NoneType]
            Time to wait between `keydown` and `keyup` in milliseconds. Defaults to 0.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        no_wait_after : Union[bool, NoneType]
            Actions that initiate navigations are waiting for these navigations to happen and for pages to start loading. You can
            opt out of waiting via setting this flag. You would only need this option in the exceptional cases such as navigating to
            inaccessible pages. Defaults to `false`.
        """

        try:
            log_api("=> frame.press started")
            result = mapping.from_maybe_impl(
                self._sync(
                    self._impl_obj.press(
                        selector=selector,
                        key=key,
                        delay=delay,
                        timeout=timeout,
                        noWaitAfter=no_wait_after,
                    )
                )
            )
            log_api("<= frame.press succeded")
            return result
        except Exception as e:
            log_api("<= frame.press failed")
            raise e

    def check(
        self,
        selector: str,
        timeout: float = None,
        force: bool = None,
        no_wait_after: bool = None,
    ) -> NoneType:
        """Frame.check

        This method checks an element matching `selector` by performing the following steps:
        1. Find an element match matching `selector`. If there is none, wait until a matching element is attached to the DOM.
        1. Ensure that matched element is a checkbox or a radio input. If not, this method rejects. If the element is already
           checked, this method returns immediately.
        1. Wait for [actionability](./actionability.md) checks on the matched element, unless `force` option is set. If the
           element is detached during the checks, the whole action is retried.
        1. Scroll the element into view if needed.
        1. Use `page.mouse` to click in the center of the element.
        1. Wait for initiated navigations to either succeed or fail, unless `noWaitAfter` option is set.
        1. Ensure that the element is now checked. If not, this method rejects.

        When all steps combined have not finished during the specified `timeout`, this method rejects with a `TimeoutError`.
        Passing zero timeout disables this.

        Parameters
        ----------
        selector : str
            A selector to search for element. If there are multiple elements satisfying the selector, the first will be used. See
            [working with selectors](./selectors.md#working-with-selectors) for more details.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        force : Union[bool, NoneType]
            Whether to bypass the [actionability](./actionability.md) checks. Defaults to `false`.
        no_wait_after : Union[bool, NoneType]
            Actions that initiate navigations are waiting for these navigations to happen and for pages to start loading. You can
            opt out of waiting via setting this flag. You would only need this option in the exceptional cases such as navigating to
            inaccessible pages. Defaults to `false`.
        """

        try:
            log_api("=> frame.check started")
            result = mapping.from_maybe_impl(
                self._sync(
                    self._impl_obj.check(
                        selector=selector,
                        timeout=timeout,
                        force=force,
                        noWaitAfter=no_wait_after,
                    )
                )
            )
            log_api("<= frame.check succeded")
            return result
        except Exception as e:
            log_api("<= frame.check failed")
            raise e

    def uncheck(
        self,
        selector: str,
        timeout: float = None,
        force: bool = None,
        no_wait_after: bool = None,
    ) -> NoneType:
        """Frame.uncheck

        This method checks an element matching `selector` by performing the following steps:
        1. Find an element match matching `selector`. If there is none, wait until a matching element is attached to the DOM.
        1. Ensure that matched element is a checkbox or a radio input. If not, this method rejects. If the element is already
           unchecked, this method returns immediately.
        1. Wait for [actionability](./actionability.md) checks on the matched element, unless `force` option is set. If the
           element is detached during the checks, the whole action is retried.
        1. Scroll the element into view if needed.
        1. Use `page.mouse` to click in the center of the element.
        1. Wait for initiated navigations to either succeed or fail, unless `noWaitAfter` option is set.
        1. Ensure that the element is now unchecked. If not, this method rejects.

        When all steps combined have not finished during the specified `timeout`, this method rejects with a `TimeoutError`.
        Passing zero timeout disables this.

        Parameters
        ----------
        selector : str
            A selector to search for element. If there are multiple elements satisfying the selector, the first will be used. See
            [working with selectors](./selectors.md#working-with-selectors) for more details.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        force : Union[bool, NoneType]
            Whether to bypass the [actionability](./actionability.md) checks. Defaults to `false`.
        no_wait_after : Union[bool, NoneType]
            Actions that initiate navigations are waiting for these navigations to happen and for pages to start loading. You can
            opt out of waiting via setting this flag. You would only need this option in the exceptional cases such as navigating to
            inaccessible pages. Defaults to `false`.
        """

        try:
            log_api("=> frame.uncheck started")
            result = mapping.from_maybe_impl(
                self._sync(
                    self._impl_obj.uncheck(
                        selector=selector,
                        timeout=timeout,
                        force=force,
                        noWaitAfter=no_wait_after,
                    )
                )
            )
            log_api("<= frame.uncheck succeded")
            return result
        except Exception as e:
            log_api("<= frame.uncheck failed")
            raise e

    def wait_for_timeout(self, timeout: float) -> NoneType:
        """Frame.wait_for_timeout

        Waits for the given `timeout` in milliseconds.

        Note that `frame.waitForTimeout()` should only be used for debugging. Tests using the timer in production are going to
        be flaky. Use signals such as network events, selectors becoming visible and others instead.

        Parameters
        ----------
        timeout : float
            A timeout to wait for
        """

        try:
            log_api("=> frame.wait_for_timeout started")
            result = mapping.from_maybe_impl(
                self._sync(self._impl_obj.wait_for_timeout(timeout=timeout))
            )
            log_api("<= frame.wait_for_timeout succeded")
            return result
        except Exception as e:
            log_api("<= frame.wait_for_timeout failed")
            raise e

    def wait_for_function(
        self,
        expression: str,
        arg: typing.Any = None,
        force_expr: bool = None,
        timeout: float = None,
        polling: typing.Union[float, Literal["raf"]] = None,
    ) -> "JSHandle":
        """Frame.wait_for_function

        Returns when the `pageFunction` returns a truthy value, returns that value.

        The `waitForFunction` can be used to observe viewport size change:

        To pass an argument to the predicate of `frame.waitForFunction` function:

        Parameters
        ----------
        expression : str
            Function to be evaluated in browser context
        force_expr : bool
            Whether to treat given expression as JavaScript evaluate expression, even though it looks like an arrow function
        arg : Union[Any, NoneType]
            Optional argument to pass to `pageFunction`
        timeout : Union[float, NoneType]
            maximum time to wait for in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default
            value can be changed by using the `browser_context.set_default_timeout()`.
        polling : Union["raf", float, NoneType]
            If `polling` is `'raf'`, then `pageFunction` is constantly executed in `requestAnimationFrame` callback. If `polling` is
            a number, then it is treated as an interval in milliseconds at which the function would be executed. Defaults to `raf`.

        Returns
        -------
        JSHandle
        """

        try:
            log_api("=> frame.wait_for_function started")
            result = mapping.from_impl(
                self._sync(
                    self._impl_obj.wait_for_function(
                        expression=expression,
                        arg=mapping.to_impl(arg),
                        force_expr=force_expr,
                        timeout=timeout,
                        polling=polling,
                    )
                )
            )
            log_api("<= frame.wait_for_function succeded")
            return result
        except Exception as e:
            log_api("<= frame.wait_for_function failed")
            raise e

    def title(self) -> str:
        """Frame.title

        Returns the page title.

        Returns
        -------
        str
        """

        try:
            log_api("=> frame.title started")
            result = mapping.from_maybe_impl(self._sync(self._impl_obj.title()))
            log_api("<= frame.title succeded")
            return result
        except Exception as e:
            log_api("<= frame.title failed")
            raise e

    def expect_load_state(
        self,
        state: Literal["domcontentloaded", "load", "networkidle"] = None,
        timeout: float = None,
    ) -> EventContextManager[typing.Union["Response", NoneType]]:
        """Frame.expect_load_state

        Returns context manager that waits for ``event`` to fire upon exit. It passes event's value
        into the ``predicate`` function and waits for the predicate to return a truthy value. Will throw
        an error if the page is closed before the ``event`` is fired.

        with page.expect_loadstate() as event_info:
            page.click("button")
        value = event_info.value

        Parameters
        ----------
        predicate : Optional[typing.Callable[[Any], bool]]
            Predicate receiving event data.
        timeout : Optional[int]
            Maximum wait time in milliseconds, defaults to 30 seconds, pass `0` to disable the timeout.
            The default value can be changed by using the browserContext.set_default_timeout(timeout) or
            page.set_default_timeout(timeout) methods.
        """
        return EventContextManager(
            self, self._impl_obj.wait_for_load_state(state, timeout)
        )

    def expect_navigation(
        self,
        url: typing.Union[str, typing.Pattern, typing.Callable[[str], bool]] = None,
        wait_until: Literal["domcontentloaded", "load", "networkidle"] = None,
        timeout: float = None,
    ) -> EventContextManager[typing.Union["Response", NoneType]]:
        """Frame.expect_navigation

        Returns context manager that waits for ``event`` to fire upon exit. It passes event's value
        into the ``predicate`` function and waits for the predicate to return a truthy value. Will throw
        an error if the page is closed before the ``event`` is fired.

        with page.expect_navigation() as event_info:
            page.click("button")
        value = event_info.value

        Parameters
        ----------
        predicate : Optional[typing.Callable[[Any], bool]]
            Predicate receiving event data.
        timeout : Optional[int]
            Maximum wait time in milliseconds, defaults to 30 seconds, pass `0` to disable the timeout.
            The default value can be changed by using the browserContext.set_default_timeout(timeout) or
            page.set_default_timeout(timeout) methods.
        """
        return EventContextManager(
            self, self._impl_obj.wait_for_navigation(url, wait_until, timeout)
        )


mapping.register(FrameImpl, Frame)


class Worker(SyncBase):
    def __init__(self, obj: WorkerImpl):
        super().__init__(obj)

    @property
    def url(self) -> str:
        """Worker.url

        Returns
        -------
        str
        """
        return mapping.from_maybe_impl(self._impl_obj.url)

    def evaluate(
        self, expression: str, arg: typing.Any = None, force_expr: bool = None
    ) -> typing.Any:
        """Worker.evaluate

        Returns the return value of `pageFunction`

        If the function passed to the `worker.evaluate` returns a [Promise], then `worker.evaluate` would wait for the promise
        to resolve and return its value.

        If the function passed to the `worker.evaluate` returns a non-[Serializable] value, then `worker.evaluate` returns
        `undefined`. DevTools Protocol also supports transferring some additional values that are not serializable by `JSON`:
        `-0`, `NaN`, `Infinity`, `-Infinity`, and bigint literals.

        Parameters
        ----------
        expression : str
            Function to be evaluated in the worker context
        force_expr : bool
            Whether to treat given expression as JavaScript evaluate expression, even though it looks like an arrow function
        arg : Union[Any, NoneType]
            Optional argument to pass to `pageFunction`

        Returns
        -------
        Any
        """

        try:
            log_api("=> worker.evaluate started")
            result = mapping.from_maybe_impl(
                self._sync(
                    self._impl_obj.evaluate(
                        expression=expression,
                        arg=mapping.to_impl(arg),
                        force_expr=force_expr,
                    )
                )
            )
            log_api("<= worker.evaluate succeded")
            return result
        except Exception as e:
            log_api("<= worker.evaluate failed")
            raise e

    def evaluate_handle(
        self, expression: str, arg: typing.Any = None, force_expr: bool = None
    ) -> "JSHandle":
        """Worker.evaluate_handle

        Returns the return value of `pageFunction` as in-page object (JSHandle).

        The only difference between `worker.evaluate` and `worker.evaluateHandle` is that `worker.evaluateHandle` returns
        in-page object (JSHandle).

        If the function passed to the `worker.evaluateHandle` returns a [Promise], then `worker.evaluateHandle` would wait for
        the promise to resolve and return its value.

        Parameters
        ----------
        expression : str
            Function to be evaluated in the page context
        force_expr : bool
            Whether to treat given expression as JavaScript evaluate expression, even though it looks like an arrow function
        arg : Union[Any, NoneType]
            Optional argument to pass to `pageFunction`

        Returns
        -------
        JSHandle
        """

        try:
            log_api("=> worker.evaluate_handle started")
            result = mapping.from_impl(
                self._sync(
                    self._impl_obj.evaluate_handle(
                        expression=expression,
                        arg=mapping.to_impl(arg),
                        force_expr=force_expr,
                    )
                )
            )
            log_api("<= worker.evaluate_handle succeded")
            return result
        except Exception as e:
            log_api("<= worker.evaluate_handle failed")
            raise e


mapping.register(WorkerImpl, Worker)


class Selectors(SyncBase):
    def __init__(self, obj: SelectorsImpl):
        super().__init__(obj)

    def register(
        self,
        name: str,
        script: str = None,
        path: typing.Union[str, pathlib.Path] = None,
        content_script: bool = None,
    ) -> NoneType:
        """Selectors.register

        An example of registering selector engine that queries elements based on a tag name:

        Parameters
        ----------
        name : str
            Name that is used in selectors as a prefix, e.g. `{name: 'foo'}` enables `foo=myselectorbody` selectors. May only
            contain `[a-zA-Z0-9_]` characters.
        script : Union[str, NoneType]
            Script that evaluates to a selector engine instance.
        content_script : Union[bool, NoneType]
            Whether to run this selector engine in isolated JavaScript environment. This environment has access to the same DOM, but
            not any JavaScript objects from the frame's scripts. Defaults to `false`. Note that running as a content script is not
            guaranteed when this engine is used together with other registered engines.
        """

        try:
            log_api("=> selectors.register started")
            result = mapping.from_maybe_impl(
                self._sync(
                    self._impl_obj.register(
                        name=name,
                        script=script,
                        path=path,
                        contentScript=content_script,
                    )
                )
            )
            log_api("<= selectors.register succeded")
            return result
        except Exception as e:
            log_api("<= selectors.register failed")
            raise e


mapping.register(SelectorsImpl, Selectors)


class ConsoleMessage(SyncBase):
    def __init__(self, obj: ConsoleMessageImpl):
        super().__init__(obj)

    @property
    def type(self) -> str:
        """ConsoleMessage.type

        One of the following values: `'log'`, `'debug'`, `'info'`, `'error'`, `'warning'`, `'dir'`, `'dirxml'`, `'table'`,
        `'trace'`, `'clear'`, `'startGroup'`, `'startGroupCollapsed'`, `'endGroup'`, `'assert'`, `'profile'`, `'profileEnd'`,
        `'count'`, `'timeEnd'`.

        Returns
        -------
        str
        """
        return mapping.from_maybe_impl(self._impl_obj.type)

    @property
    def text(self) -> str:
        """ConsoleMessage.text

        Returns
        -------
        str
        """
        return mapping.from_maybe_impl(self._impl_obj.text)

    @property
    def args(self) -> typing.List["JSHandle"]:
        """ConsoleMessage.args

        Returns
        -------
        List[JSHandle]
        """
        return mapping.from_impl_list(self._impl_obj.args)

    @property
    def location(self) -> "SourceLocation":
        """ConsoleMessage.location

        Returns
        -------
        {url: str, line_number: int, column_number: int}
        """
        return mapping.from_impl(self._impl_obj.location)


mapping.register(ConsoleMessageImpl, ConsoleMessage)


class Dialog(SyncBase):
    def __init__(self, obj: DialogImpl):
        super().__init__(obj)

    @property
    def type(self) -> str:
        """Dialog.type

        Returns dialog's type, can be one of `alert`, `beforeunload`, `confirm` or `prompt`.

        Returns
        -------
        str
        """
        return mapping.from_maybe_impl(self._impl_obj.type)

    @property
    def message(self) -> str:
        """Dialog.message

        A message displayed in the dialog.

        Returns
        -------
        str
        """
        return mapping.from_maybe_impl(self._impl_obj.message)

    @property
    def default_value(self) -> str:
        """Dialog.default_value

        If dialog is prompt, returns default prompt value. Otherwise, returns empty string.

        Returns
        -------
        str
        """
        return mapping.from_maybe_impl(self._impl_obj.default_value)

    def accept(self, prompt_text: str = None) -> NoneType:
        """Dialog.accept

        Returns when the dialog has been accepted.

        Parameters
        ----------
        prompt_text : Union[str, NoneType]
            A text to enter in prompt. Does not cause any effects if the dialog's `type` is not prompt. Optional.
        """

        try:
            log_api("=> dialog.accept started")
            result = mapping.from_maybe_impl(
                self._sync(self._impl_obj.accept(promptText=prompt_text))
            )
            log_api("<= dialog.accept succeded")
            return result
        except Exception as e:
            log_api("<= dialog.accept failed")
            raise e

    def dismiss(self) -> NoneType:
        """Dialog.dismiss

        Returns when the dialog has been dismissed.
        """

        try:
            log_api("=> dialog.dismiss started")
            result = mapping.from_maybe_impl(self._sync(self._impl_obj.dismiss()))
            log_api("<= dialog.dismiss succeded")
            return result
        except Exception as e:
            log_api("<= dialog.dismiss failed")
            raise e


mapping.register(DialogImpl, Dialog)


class Download(SyncBase):
    def __init__(self, obj: DownloadImpl):
        super().__init__(obj)

    @property
    def url(self) -> str:
        """Download.url

        Returns downloaded url.

        Returns
        -------
        str
        """
        return mapping.from_maybe_impl(self._impl_obj.url)

    @property
    def suggested_filename(self) -> str:
        """Download.suggested_filename

        Returns suggested filename for this download. It is typically computed by the browser from the
        [`Content-Disposition`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Disposition) response header
        or the `download` attribute. See the spec on [whatwg](https://html.spec.whatwg.org/#downloading-resources). Different
        browsers can use different logic for computing it.

        Returns
        -------
        str
        """
        return mapping.from_maybe_impl(self._impl_obj.suggested_filename)

    def delete(self) -> NoneType:
        """Download.delete

        Deletes the downloaded file.
        """

        try:
            log_api("=> download.delete started")
            result = mapping.from_maybe_impl(self._sync(self._impl_obj.delete()))
            log_api("<= download.delete succeded")
            return result
        except Exception as e:
            log_api("<= download.delete failed")
            raise e

    def failure(self) -> typing.Union[str, NoneType]:
        """Download.failure

        Returns download error if any.

        Returns
        -------
        Union[str, NoneType]
        """

        try:
            log_api("=> download.failure started")
            result = mapping.from_maybe_impl(self._sync(self._impl_obj.failure()))
            log_api("<= download.failure succeded")
            return result
        except Exception as e:
            log_api("<= download.failure failed")
            raise e

    def path(self) -> typing.Union[str, NoneType]:
        """Download.path

        Returns path to the downloaded file in case of successful download.

        Returns
        -------
        Union[str, NoneType]
        """

        try:
            log_api("=> download.path started")
            result = mapping.from_maybe_impl(self._sync(self._impl_obj.path()))
            log_api("<= download.path succeded")
            return result
        except Exception as e:
            log_api("<= download.path failed")
            raise e

    def save_as(self, path: typing.Union[str, pathlib.Path]) -> NoneType:
        """Download.save_as

        Saves the download to a user-specified path.

        Parameters
        ----------
        path : Union[pathlib.Path, str]
            Path where the download should be saved.
        """

        try:
            log_api("=> download.save_as started")
            result = mapping.from_maybe_impl(
                self._sync(self._impl_obj.save_as(path=path))
            )
            log_api("<= download.save_as succeded")
            return result
        except Exception as e:
            log_api("<= download.save_as failed")
            raise e


mapping.register(DownloadImpl, Download)


class Video(SyncBase):
    def __init__(self, obj: VideoImpl):
        super().__init__(obj)

    def path(self) -> str:
        """Video.path

        Returns the file system path this video will be recorded to. The video is guaranteed to be written to the filesystem
        upon closing the browser context.

        Returns
        -------
        str
        """

        try:
            log_api("=> video.path started")
            result = mapping.from_maybe_impl(self._sync(self._impl_obj.path()))
            log_api("<= video.path succeded")
            return result
        except Exception as e:
            log_api("<= video.path failed")
            raise e


mapping.register(VideoImpl, Video)


class BindingCall(SyncBase):
    def __init__(self, obj: BindingCallImpl):
        super().__init__(obj)

    def call(self, func: typing.Callable) -> NoneType:

        try:
            log_api("=> binding_call.call started")
            result = mapping.from_maybe_impl(
                self._sync(self._impl_obj.call(func=self._wrap_handler(func)))
            )
            log_api("<= binding_call.call succeded")
            return result
        except Exception as e:
            log_api("<= binding_call.call failed")
            raise e


mapping.register(BindingCallImpl, BindingCall)


class Page(SyncBase):
    def __init__(self, obj: PageImpl):
        super().__init__(obj)

    @property
    def accessibility(self) -> "Accessibility":
        """Page.accessibility

        Returns
        -------
        Accessibility
        """
        return mapping.from_impl(self._impl_obj.accessibility)

    @property
    def keyboard(self) -> "Keyboard":
        """Page.keyboard

        Returns
        -------
        Keyboard
        """
        return mapping.from_impl(self._impl_obj.keyboard)

    @property
    def mouse(self) -> "Mouse":
        """Page.mouse

        Returns
        -------
        Mouse
        """
        return mapping.from_impl(self._impl_obj.mouse)

    @property
    def touchscreen(self) -> "Touchscreen":
        """Page.touchscreen

        Returns
        -------
        Touchscreen
        """
        return mapping.from_impl(self._impl_obj.touchscreen)

    @property
    def context(self) -> "BrowserContext":
        """Page.context

        Get the browser context that the page belongs to.

        Returns
        -------
        BrowserContext
        """
        return mapping.from_impl(self._impl_obj.context)

    @property
    def main_frame(self) -> "Frame":
        """Page.main_frame

        The page's main frame. Page is guaranteed to have a main frame which persists during navigations.

        Returns
        -------
        Frame
        """
        return mapping.from_impl(self._impl_obj.main_frame)

    @property
    def frames(self) -> typing.List["Frame"]:
        """Page.frames

        An array of all frames attached to the page.

        Returns
        -------
        List[Frame]
        """
        return mapping.from_impl_list(self._impl_obj.frames)

    @property
    def url(self) -> str:
        """Page.url

        Shortcut for main frame's `frame.url()`.

        Returns
        -------
        str
        """
        return mapping.from_maybe_impl(self._impl_obj.url)

    @property
    def workers(self) -> typing.List["Worker"]:
        """Page.workers

        This method returns all of the dedicated [WebWorkers](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API)
        associated with the page.

        > **NOTE** This does not contain ServiceWorkers

        Returns
        -------
        List[Worker]
        """
        return mapping.from_impl_list(self._impl_obj.workers)

    @property
    def video(self) -> typing.Union["Video", NoneType]:
        """Page.video

        Video object associated with this page.

        Returns
        -------
        Union[Video, NoneType]
        """
        return mapping.from_impl_nullable(self._impl_obj.video)

    def opener(self) -> typing.Union["Page", NoneType]:
        """Page.opener

        Returns the opener for popup pages and `null` for others. If the opener has been closed already the returns `null`.

        Returns
        -------
        Union[Page, NoneType]
        """

        try:
            log_api("=> page.opener started")
            result = mapping.from_impl_nullable(self._sync(self._impl_obj.opener()))
            log_api("<= page.opener succeded")
            return result
        except Exception as e:
            log_api("<= page.opener failed")
            raise e

    def frame(
        self,
        name: str = None,
        url: typing.Union[str, typing.Pattern, typing.Callable[[str], bool]] = None,
    ) -> typing.Union["Frame", NoneType]:
        """Page.frame

        Returns frame matching the specified criteria. Either `name` or `url` must be specified.

        Parameters
        ----------
        name : Union[str, NoneType]
            Frame name specified in the `iframe`'s `name` attribute. Optional.
        url : Union[Callable[[str], bool], Pattern, str, NoneType]
            A glob pattern, regex pattern or predicate receiving frame's `url` as a [URL] object. Optional.

        Returns
        -------
        Union[Frame, NoneType]
        """

        try:
            log_api("=> page.frame started")
            result = mapping.from_impl_nullable(
                self._impl_obj.frame(name=name, url=self._wrap_handler(url))
            )
            log_api("<= page.frame succeded")
            return result
        except Exception as e:
            log_api("<= page.frame failed")
            raise e

    def set_default_navigation_timeout(self, timeout: float) -> NoneType:
        """Page.set_default_navigation_timeout

        This setting will change the default maximum navigation time for the following methods and related shortcuts:
        - `page.go_back()`
        - `page.go_forward()`
        - `page.goto()`
        - `page.reload()`
        - `page.set_content()`
        - `page.wait_for_navigation()`

        > **NOTE** `page.set_default_navigation_timeout()` takes priority over `page.set_default_timeout()`,
        `browser_context.set_default_timeout()` and `browser_context.set_default_navigation_timeout()`.

        Parameters
        ----------
        timeout : float
            Maximum navigation time in milliseconds
        """

        try:
            log_api("=> page.set_default_navigation_timeout started")
            result = mapping.from_maybe_impl(
                self._impl_obj.set_default_navigation_timeout(timeout=timeout)
            )
            log_api("<= page.set_default_navigation_timeout succeded")
            return result
        except Exception as e:
            log_api("<= page.set_default_navigation_timeout failed")
            raise e

    def set_default_timeout(self, timeout: float) -> NoneType:
        """Page.set_default_timeout

        This setting will change the default maximum time for all the methods accepting `timeout` option.

        > **NOTE** `page.set_default_navigation_timeout()` takes priority over `page.set_default_timeout()`.

        Parameters
        ----------
        timeout : float
            Maximum time in milliseconds
        """

        try:
            log_api("=> page.set_default_timeout started")
            result = mapping.from_maybe_impl(
                self._impl_obj.set_default_timeout(timeout=timeout)
            )
            log_api("<= page.set_default_timeout succeded")
            return result
        except Exception as e:
            log_api("<= page.set_default_timeout failed")
            raise e

    def query_selector(self, selector: str) -> typing.Union["ElementHandle", NoneType]:
        """Page.query_selector

        The method finds an element matching the specified selector within the page. If no elements match the selector, the
        return value resolves to `null`.

        Shortcut for main frame's `frame.$()`.

        Parameters
        ----------
        selector : str
            A selector to query for. See [working with selectors](./selectors.md#working-with-selectors) for more details.

        Returns
        -------
        Union[ElementHandle, NoneType]
        """

        try:
            log_api("=> page.query_selector started")
            result = mapping.from_impl_nullable(
                self._sync(self._impl_obj.query_selector(selector=selector))
            )
            log_api("<= page.query_selector succeded")
            return result
        except Exception as e:
            log_api("<= page.query_selector failed")
            raise e

    def query_selector_all(self, selector: str) -> typing.List["ElementHandle"]:
        """Page.query_selector_all

        The method finds all elements matching the specified selector within the page. If no elements match the selector, the
        return value resolves to `[]`.

        Shortcut for main frame's `frame.$$()`.

        Parameters
        ----------
        selector : str
            A selector to query for. See [working with selectors](./selectors.md#working-with-selectors) for more details.

        Returns
        -------
        List[ElementHandle]
        """

        try:
            log_api("=> page.query_selector_all started")
            result = mapping.from_impl_list(
                self._sync(self._impl_obj.query_selector_all(selector=selector))
            )
            log_api("<= page.query_selector_all succeded")
            return result
        except Exception as e:
            log_api("<= page.query_selector_all failed")
            raise e

    def wait_for_selector(
        self,
        selector: str,
        timeout: float = None,
        state: Literal["attached", "detached", "hidden", "visible"] = None,
    ) -> typing.Union["ElementHandle", NoneType]:
        """Page.wait_for_selector

        Returns when element specified by selector satisfies `state` option. Returns `null` if waiting for `hidden` or
        `detached`.

        Wait for the `selector` to satisfy `state` option (either appear/disappear from dom, or become visible/hidden). If at
        the moment of calling the method `selector` already satisfies the condition, the method will return immediately. If the
        selector doesn't satisfy the condition for the `timeout` milliseconds, the function will throw.

        This method works across navigations:

        Parameters
        ----------
        selector : str
            A selector to query for. See [working with selectors](./selectors.md#working-with-selectors) for more details.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        state : Union["attached", "detached", "hidden", "visible", NoneType]
            Defaults to `'visible'`. Can be either:
            - `'attached'` - wait for element to be present in DOM.
            - `'detached'` - wait for element to not be present in DOM.
            - `'visible'` - wait for element to have non-empty bounding box and no `visibility:hidden`. Note that element without
              any content or with `display:none` has an empty bounding box and is not considered visible.
            - `'hidden'` - wait for element to be either detached from DOM, or have an empty bounding box or `visibility:hidden`.
              This is opposite to the `'visible'` option.

        Returns
        -------
        Union[ElementHandle, NoneType]
        """

        try:
            log_api("=> page.wait_for_selector started")
            result = mapping.from_impl_nullable(
                self._sync(
                    self._impl_obj.wait_for_selector(
                        selector=selector, timeout=timeout, state=state
                    )
                )
            )
            log_api("<= page.wait_for_selector succeded")
            return result
        except Exception as e:
            log_api("<= page.wait_for_selector failed")
            raise e

    def dispatch_event(
        self,
        selector: str,
        type: str,
        event_init: typing.Dict = None,
        timeout: float = None,
    ) -> NoneType:
        """Page.dispatch_event

        The snippet below dispatches the `click` event on the element. Regardless of the visibility state of the elment, `click`
        is dispatched. This is equivalend to calling
        [element.click()](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/click).

        Under the hood, it creates an instance of an event based on the given `type`, initializes it with `eventInit` properties
        and dispatches it on the element. Events are `composed`, `cancelable` and bubble by default.

        Since `eventInit` is event-specific, please refer to the events documentation for the lists of initial properties:
        - [DragEvent](https://developer.mozilla.org/en-US/docs/Web/API/DragEvent/DragEvent)
        - [FocusEvent](https://developer.mozilla.org/en-US/docs/Web/API/FocusEvent/FocusEvent)
        - [KeyboardEvent](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/KeyboardEvent)
        - [MouseEvent](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/MouseEvent)
        - [PointerEvent](https://developer.mozilla.org/en-US/docs/Web/API/PointerEvent/PointerEvent)
        - [TouchEvent](https://developer.mozilla.org/en-US/docs/Web/API/TouchEvent/TouchEvent)
        - [Event](https://developer.mozilla.org/en-US/docs/Web/API/Event/Event)

        You can also specify `JSHandle` as the property value if you want live objects to be passed into the event:

        Parameters
        ----------
        selector : str
            A selector to search for element. If there are multiple elements satisfying the selector, the first will be used. See
            [working with selectors](./selectors.md#working-with-selectors) for more details.
        type : str
            DOM event type: `"click"`, `"dragstart"`, etc.
        event_init : Union[Dict, NoneType]
            Optional event-specific initialization properties.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        """

        try:
            log_api("=> page.dispatch_event started")
            result = mapping.from_maybe_impl(
                self._sync(
                    self._impl_obj.dispatch_event(
                        selector=selector,
                        type=type,
                        eventInit=mapping.to_impl(event_init),
                        timeout=timeout,
                    )
                )
            )
            log_api("<= page.dispatch_event succeded")
            return result
        except Exception as e:
            log_api("<= page.dispatch_event failed")
            raise e

    def evaluate(
        self, expression: str, arg: typing.Any = None, force_expr: bool = None
    ) -> typing.Any:
        """Page.evaluate

        Returns the value of the `pageFunction` invocation.

        If the function passed to the `page.evaluate` returns a [Promise], then `page.evaluate` would wait for the promise to
        resolve and return its value.

        If the function passed to the `page.evaluate` returns a non-[Serializable] value, then `page.evaluate` resolves to
        `undefined`. DevTools Protocol also supports transferring some additional values that are not serializable by `JSON`:
        `-0`, `NaN`, `Infinity`, `-Infinity`, and bigint literals.

        Passing argument to `pageFunction`:

        A string can also be passed in instead of a function:

        `ElementHandle` instances can be passed as an argument to the `page.evaluate`:

        Shortcut for main frame's `frame.evaluate()`.

        Parameters
        ----------
        expression : str
            Function to be evaluated in the page context
        force_expr : bool
            Whether to treat given expression as JavaScript evaluate expression, even though it looks like an arrow function
        arg : Union[Any, NoneType]
            Optional argument to pass to `pageFunction`

        Returns
        -------
        Any
        """

        try:
            log_api("=> page.evaluate started")
            result = mapping.from_maybe_impl(
                self._sync(
                    self._impl_obj.evaluate(
                        expression=expression,
                        arg=mapping.to_impl(arg),
                        force_expr=force_expr,
                    )
                )
            )
            log_api("<= page.evaluate succeded")
            return result
        except Exception as e:
            log_api("<= page.evaluate failed")
            raise e

    def evaluate_handle(
        self, expression: str, arg: typing.Any = None, force_expr: bool = None
    ) -> "JSHandle":
        """Page.evaluate_handle

        Returns the value of the `pageFunction` invocation as in-page object (JSHandle).

        The only difference between `page.evaluate` and `page.evaluateHandle` is that `page.evaluateHandle` returns in-page
        object (JSHandle).

        If the function passed to the `page.evaluateHandle` returns a [Promise], then `page.evaluateHandle` would wait for the
        promise to resolve and return its value.

        A string can also be passed in instead of a function:

        `JSHandle` instances can be passed as an argument to the `page.evaluateHandle`:

        Parameters
        ----------
        expression : str
            Function to be evaluated in the page context
        force_expr : bool
            Whether to treat given expression as JavaScript evaluate expression, even though it looks like an arrow function
        arg : Union[Any, NoneType]
            Optional argument to pass to `pageFunction`

        Returns
        -------
        JSHandle
        """

        try:
            log_api("=> page.evaluate_handle started")
            result = mapping.from_impl(
                self._sync(
                    self._impl_obj.evaluate_handle(
                        expression=expression,
                        arg=mapping.to_impl(arg),
                        force_expr=force_expr,
                    )
                )
            )
            log_api("<= page.evaluate_handle succeded")
            return result
        except Exception as e:
            log_api("<= page.evaluate_handle failed")
            raise e

    def eval_on_selector(
        self,
        selector: str,
        expression: str,
        arg: typing.Any = None,
        force_expr: bool = None,
    ) -> typing.Any:
        """Page.eval_on_selector

        The method finds an element matching the specified selector within the page and passes it as a first argument to
        `pageFunction`. If no elements match the selector, the method throws an error. Returns the value of `pageFunction`.

        If `pageFunction` returns a [Promise], then `page.$eval()` would wait for the promise to resolve and return its
        value.

        Examples:

        Shortcut for main frame's `frame.$eval()`.

        Parameters
        ----------
        selector : str
            A selector to query for. See [working with selectors](./selectors.md#working-with-selectors) for more details.
        expression : str
            Function to be evaluated in browser context
        force_expr : bool
            Whether to treat given expression as JavaScript evaluate expression, even though it looks like an arrow function
        arg : Union[Any, NoneType]
            Optional argument to pass to `pageFunction`

        Returns
        -------
        Any
        """

        try:
            log_api("=> page.eval_on_selector started")
            result = mapping.from_maybe_impl(
                self._sync(
                    self._impl_obj.eval_on_selector(
                        selector=selector,
                        expression=expression,
                        arg=mapping.to_impl(arg),
                        force_expr=force_expr,
                    )
                )
            )
            log_api("<= page.eval_on_selector succeded")
            return result
        except Exception as e:
            log_api("<= page.eval_on_selector failed")
            raise e

    def eval_on_selector_all(
        self,
        selector: str,
        expression: str,
        arg: typing.Any = None,
        force_expr: bool = None,
    ) -> typing.Any:
        """Page.eval_on_selector_all

        The method finds all elements matching the specified selector within the page and passes an array of matched elements as
        a first argument to `pageFunction`. Returns the result of `pageFunction` invocation.

        If `pageFunction` returns a [Promise], then `page.$$eval()` would wait for the promise to resolve and return its
        value.

        Examples:

        Parameters
        ----------
        selector : str
            A selector to query for. See [working with selectors](./selectors.md#working-with-selectors) for more details.
        expression : str
            Function to be evaluated in browser context
        force_expr : bool
            Whether to treat given expression as JavaScript evaluate expression, even though it looks like an arrow function
        arg : Union[Any, NoneType]
            Optional argument to pass to `pageFunction`

        Returns
        -------
        Any
        """

        try:
            log_api("=> page.eval_on_selector_all started")
            result = mapping.from_maybe_impl(
                self._sync(
                    self._impl_obj.eval_on_selector_all(
                        selector=selector,
                        expression=expression,
                        arg=mapping.to_impl(arg),
                        force_expr=force_expr,
                    )
                )
            )
            log_api("<= page.eval_on_selector_all succeded")
            return result
        except Exception as e:
            log_api("<= page.eval_on_selector_all failed")
            raise e

    def add_script_tag(
        self,
        url: str = None,
        path: typing.Union[str, pathlib.Path] = None,
        content: str = None,
        type: str = None,
    ) -> "ElementHandle":
        """Page.add_script_tag

        Adds a `<script>` tag into the page with the desired url or content. Returns the added tag when the script's onload
        fires or when the script content was injected into frame.

        Shortcut for main frame's `frame.add_script_tag()`.

        Parameters
        ----------
        url : Union[str, NoneType]
            URL of a script to be added. Optional.
        path : Union[pathlib.Path, str, NoneType]
            Path to the JavaScript file to be injected into frame. If `path` is a relative path, then it is resolved relative to the
            current working directory. Optional.
        content : Union[str, NoneType]
            Raw JavaScript content to be injected into frame. Optional.
        type : Union[str, NoneType]
            Script type. Use 'module' in order to load a Javascript ES6 module. See
            [script](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/script) for more details. Optional.

        Returns
        -------
        ElementHandle
        """

        try:
            log_api("=> page.add_script_tag started")
            result = mapping.from_impl(
                self._sync(
                    self._impl_obj.add_script_tag(
                        url=url, path=path, content=content, type=type
                    )
                )
            )
            log_api("<= page.add_script_tag succeded")
            return result
        except Exception as e:
            log_api("<= page.add_script_tag failed")
            raise e

    def add_style_tag(
        self,
        url: str = None,
        path: typing.Union[str, pathlib.Path] = None,
        content: str = None,
    ) -> "ElementHandle":
        """Page.add_style_tag

        Adds a `<link rel="stylesheet">` tag into the page with the desired url or a `<style type="text/css">` tag with the
        content. Returns the added tag when the stylesheet's onload fires or when the CSS content was injected into frame.

        Shortcut for main frame's `frame.add_style_tag()`.

        Parameters
        ----------
        url : Union[str, NoneType]
            URL of the `<link>` tag. Optional.
        path : Union[pathlib.Path, str, NoneType]
            Path to the CSS file to be injected into frame. If `path` is a relative path, then it is resolved relative to the
            current working directory. Optional.
        content : Union[str, NoneType]
            Raw CSS content to be injected into frame. Optional.

        Returns
        -------
        ElementHandle
        """

        try:
            log_api("=> page.add_style_tag started")
            result = mapping.from_impl(
                self._sync(
                    self._impl_obj.add_style_tag(url=url, path=path, content=content)
                )
            )
            log_api("<= page.add_style_tag succeded")
            return result
        except Exception as e:
            log_api("<= page.add_style_tag failed")
            raise e

    def expose_function(self, name: str, callback: typing.Callable) -> NoneType:
        """Page.expose_function

        The method adds a function called `name` on the `window` object of every frame in the page. When called, the function
        executes `callback` and returns a [Promise] which resolves to the return value of `callback`.

        If the `callback` returns a [Promise], it will be awaited.

        See `browser_context.expose_function()` for context-wide exposed function.

        > **NOTE** Functions installed via `page.exposeFunction` survive navigations.

        An example of adding an `md5` function to the page:

        An example of adding a `window.readfile` function to the page:

        Parameters
        ----------
        name : str
            Name of the function on the window object
        callback : Callable
            Callback function which will be called in Playwright's context.
        """

        try:
            log_api("=> page.expose_function started")
            result = mapping.from_maybe_impl(
                self._sync(
                    self._impl_obj.expose_function(
                        name=name, callback=self._wrap_handler(callback)
                    )
                )
            )
            log_api("<= page.expose_function succeded")
            return result
        except Exception as e:
            log_api("<= page.expose_function failed")
            raise e

    def expose_binding(
        self, name: str, callback: typing.Callable, handle: bool = None
    ) -> NoneType:
        """Page.expose_binding

        The method adds a function called `name` on the `window` object of every frame in this page. When called, the function
        executes `callback` and returns a [Promise] which resolves to the return value of `callback`. If the `callback` returns
        a [Promise], it will be awaited.

        The first argument of the `callback` function contains information about the caller: `{ browserContext: BrowserContext,
        page: Page, frame: Frame }`.

        See `browser_context.expose_binding()` for the context-wide version.

        > **NOTE** Functions installed via `page.exposeBinding` survive navigations.

        An example of exposing page URL to all frames in a page:

        An example of passing an element handle:

        Parameters
        ----------
        name : str
            Name of the function on the window object.
        callback : Callable
            Callback function that will be called in the Playwright's context.
        handle : Union[bool, NoneType]
            Whether to pass the argument as a handle, instead of passing by value. When passing a handle, only one argument is
            supported. When passing by value, multiple arguments are supported.
        """

        try:
            log_api("=> page.expose_binding started")
            result = mapping.from_maybe_impl(
                self._sync(
                    self._impl_obj.expose_binding(
                        name=name, callback=self._wrap_handler(callback), handle=handle
                    )
                )
            )
            log_api("<= page.expose_binding succeded")
            return result
        except Exception as e:
            log_api("<= page.expose_binding failed")
            raise e

    def set_extra_http_headers(self, headers: typing.Dict[str, str]) -> NoneType:
        """Page.set_extra_http_headers

        The extra HTTP headers will be sent with every request the page initiates.

        > **NOTE** page.setExtraHTTPHeaders does not guarantee the order of headers in the outgoing requests.

        Parameters
        ----------
        headers : Dict[str, str]
            An object containing additional HTTP headers to be sent with every request. All header values must be strings.
        """

        try:
            log_api("=> page.set_extra_http_headers started")
            result = mapping.from_maybe_impl(
                self._sync(
                    self._impl_obj.set_extra_http_headers(
                        headers=mapping.to_impl(headers)
                    )
                )
            )
            log_api("<= page.set_extra_http_headers succeded")
            return result
        except Exception as e:
            log_api("<= page.set_extra_http_headers failed")
            raise e

    def content(self) -> str:
        """Page.content

        Gets the full HTML contents of the page, including the doctype.

        Returns
        -------
        str
        """

        try:
            log_api("=> page.content started")
            result = mapping.from_maybe_impl(self._sync(self._impl_obj.content()))
            log_api("<= page.content succeded")
            return result
        except Exception as e:
            log_api("<= page.content failed")
            raise e

    def set_content(
        self,
        html: str,
        timeout: float = None,
        wait_until: Literal["domcontentloaded", "load", "networkidle"] = None,
    ) -> NoneType:
        """Page.set_content

        Parameters
        ----------
        html : str
            HTML markup to assign to the page.
        timeout : Union[float, NoneType]
            Maximum operation time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be
            changed by using the `browser_context.set_default_navigation_timeout()`,
            `browser_context.set_default_timeout()`, `page.set_default_navigation_timeout()` or
            `page.set_default_timeout()` methods.
        wait_until : Union["domcontentloaded", "load", "networkidle", NoneType]
            When to consider operation succeeded, defaults to `load`. Events can be either:
            - `'domcontentloaded'` - consider operation to be finished when the `DOMContentLoaded` event is fired.
            - `'load'` - consider operation to be finished when the `load` event is fired.
            - `'networkidle'` - consider operation to be finished when there are no network connections for at least `500` ms.
        """

        try:
            log_api("=> page.set_content started")
            result = mapping.from_maybe_impl(
                self._sync(
                    self._impl_obj.set_content(
                        html=html, timeout=timeout, waitUntil=wait_until
                    )
                )
            )
            log_api("<= page.set_content succeded")
            return result
        except Exception as e:
            log_api("<= page.set_content failed")
            raise e

    def goto(
        self,
        url: str,
        timeout: float = None,
        wait_until: Literal["domcontentloaded", "load", "networkidle"] = None,
        referer: str = None,
    ) -> typing.Union["Response", NoneType]:
        """Page.goto

        Returns the main resource response. In case of multiple redirects, the navigation will resolve with the response of the
        last redirect.

        `page.goto` will throw an error if:
        - there's an SSL error (e.g. in case of self-signed certificates).
        - target URL is invalid.
        - the `timeout` is exceeded during navigation.
        - the remote server does not respond or is unreachable.
        - the main resource failed to load.

        `page.goto` will not throw an error when any valid HTTP status code is returned by the remote server, including 404 "Not
        Found" and 500 "Internal Server Error".  The status code for such responses can be retrieved by calling
        `response.status()`.

        > **NOTE** `page.goto` either throws an error or returns a main resource response. The only exceptions are navigation to
        `about:blank` or navigation to the same URL with a different hash, which would succeed and return `null`.
        > **NOTE** Headless mode doesn't support navigation to a PDF document. See the
        [upstream issue](https://bugs.chromium.org/p/chromium/issues/detail?id=761295).

        Shortcut for main frame's `frame.goto()`

        Parameters
        ----------
        url : str
            URL to navigate page to. The url should include scheme, e.g. `https://`.
        timeout : Union[float, NoneType]
            Maximum operation time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be
            changed by using the `browser_context.set_default_navigation_timeout()`,
            `browser_context.set_default_timeout()`, `page.set_default_navigation_timeout()` or
            `page.set_default_timeout()` methods.
        wait_until : Union["domcontentloaded", "load", "networkidle", NoneType]
            When to consider operation succeeded, defaults to `load`. Events can be either:
            - `'domcontentloaded'` - consider operation to be finished when the `DOMContentLoaded` event is fired.
            - `'load'` - consider operation to be finished when the `load` event is fired.
            - `'networkidle'` - consider operation to be finished when there are no network connections for at least `500` ms.
        referer : Union[str, NoneType]
            Referer header value. If provided it will take preference over the referer header value set by
            `page.set_extra_http_headers()`.

        Returns
        -------
        Union[Response, NoneType]
        """

        try:
            log_api("=> page.goto started")
            result = mapping.from_impl_nullable(
                self._sync(
                    self._impl_obj.goto(
                        url=url, timeout=timeout, waitUntil=wait_until, referer=referer
                    )
                )
            )
            log_api("<= page.goto succeded")
            return result
        except Exception as e:
            log_api("<= page.goto failed")
            raise e

    def reload(
        self,
        timeout: float = None,
        wait_until: Literal["domcontentloaded", "load", "networkidle"] = None,
    ) -> typing.Union["Response", NoneType]:
        """Page.reload

        Returns the main resource response. In case of multiple redirects, the navigation will resolve with the response of the
        last redirect.

        Parameters
        ----------
        timeout : Union[float, NoneType]
            Maximum operation time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be
            changed by using the `browser_context.set_default_navigation_timeout()`,
            `browser_context.set_default_timeout()`, `page.set_default_navigation_timeout()` or
            `page.set_default_timeout()` methods.
        wait_until : Union["domcontentloaded", "load", "networkidle", NoneType]
            When to consider operation succeeded, defaults to `load`. Events can be either:
            - `'domcontentloaded'` - consider operation to be finished when the `DOMContentLoaded` event is fired.
            - `'load'` - consider operation to be finished when the `load` event is fired.
            - `'networkidle'` - consider operation to be finished when there are no network connections for at least `500` ms.

        Returns
        -------
        Union[Response, NoneType]
        """

        try:
            log_api("=> page.reload started")
            result = mapping.from_impl_nullable(
                self._sync(self._impl_obj.reload(timeout=timeout, waitUntil=wait_until))
            )
            log_api("<= page.reload succeded")
            return result
        except Exception as e:
            log_api("<= page.reload failed")
            raise e

    def wait_for_load_state(
        self,
        state: Literal["domcontentloaded", "load", "networkidle"] = None,
        timeout: float = None,
    ) -> NoneType:
        """Page.wait_for_load_state

        Returns when the required load state has been reached.

        This resolves when the page reaches a required load state, `load` by default. The navigation must have been committed
        when this method is called. If current document has already reached the required state, resolves immediately.

        Shortcut for main frame's `frame.wait_for_load_state()`.

        Parameters
        ----------
        state : Union["domcontentloaded", "load", "networkidle", NoneType]
            Optional load state to wait for, defaults to `load`. If the state has been already reached while loading current
            document, the method resolves immediately. Can be one of:
            - `'load'` - wait for the `load` event to be fired.
            - `'domcontentloaded'` - wait for the `DOMContentLoaded` event to be fired.
            - `'networkidle'` - wait until there are no network connections for at least `500` ms.
        timeout : Union[float, NoneType]
            Maximum operation time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be
            changed by using the `browser_context.set_default_navigation_timeout()`,
            `browser_context.set_default_timeout()`, `page.set_default_navigation_timeout()` or
            `page.set_default_timeout()` methods.
        """

        try:
            log_api("=> page.wait_for_load_state started")
            result = mapping.from_maybe_impl(
                self._sync(
                    self._impl_obj.wait_for_load_state(state=state, timeout=timeout)
                )
            )
            log_api("<= page.wait_for_load_state succeded")
            return result
        except Exception as e:
            log_api("<= page.wait_for_load_state failed")
            raise e

    def wait_for_navigation(
        self,
        url: typing.Union[str, typing.Pattern, typing.Callable[[str], bool]] = None,
        wait_until: Literal["domcontentloaded", "load", "networkidle"] = None,
        timeout: float = None,
    ) -> typing.Union["Response", NoneType]:
        """Page.wait_for_navigation

        Returns the main resource response. In case of multiple redirects, the navigation will resolve with the response of the
        last redirect. In case of navigation to a different anchor or navigation due to History API usage, the navigation will
        resolve with `null`.

        This resolves when the page navigates to a new URL or reloads. It is useful for when you run code which will indirectly
        cause the page to navigate. e.g. The click target has an `onclick` handler that triggers navigation from a `setTimeout`.
        Consider this example:

        **NOTE** Usage of the [History API](https://developer.mozilla.org/en-US/docs/Web/API/History_API) to change the URL is
        considered a navigation.

        Shortcut for main frame's `frame.wait_for_navigation()`.

        Parameters
        ----------
        url : Union[Callable[[str], bool], Pattern, str, NoneType]
            A glob pattern, regex pattern or predicate receiving [URL] to match while waiting for the navigation.
        wait_until : Union["domcontentloaded", "load", "networkidle", NoneType]
            When to consider operation succeeded, defaults to `load`. Events can be either:
            - `'domcontentloaded'` - consider operation to be finished when the `DOMContentLoaded` event is fired.
            - `'load'` - consider operation to be finished when the `load` event is fired.
            - `'networkidle'` - consider operation to be finished when there are no network connections for at least `500` ms.
        timeout : Union[float, NoneType]
            Maximum operation time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be
            changed by using the `browser_context.set_default_navigation_timeout()`,
            `browser_context.set_default_timeout()`, `page.set_default_navigation_timeout()` or
            `page.set_default_timeout()` methods.

        Returns
        -------
        Union[Response, NoneType]
        """

        try:
            log_api("=> page.wait_for_navigation started")
            result = mapping.from_impl_nullable(
                self._sync(
                    self._impl_obj.wait_for_navigation(
                        url=self._wrap_handler(url),
                        waitUntil=wait_until,
                        timeout=timeout,
                    )
                )
            )
            log_api("<= page.wait_for_navigation succeded")
            return result
        except Exception as e:
            log_api("<= page.wait_for_navigation failed")
            raise e

    def wait_for_request(
        self,
        url_or_predicate: typing.Union[
            str, typing.Pattern, typing.Callable[["Request"], bool]
        ],
        timeout: float = None,
    ) -> "Request":
        """Page.wait_for_request

        Waits for the matching request and returns it.

        Parameters
        ----------
        url_or_predicate : Union[Callable[[Request], bool], Pattern, str]
            Request URL string, regex or predicate receiving `Request` object.
        timeout : Union[float, NoneType]
            Maximum wait time in milliseconds, defaults to 30 seconds, pass `0` to disable the timeout. The default value can be
            changed by using the `page.set_default_timeout()` method.

        Returns
        -------
        Request
        """

        try:
            log_api("=> page.wait_for_request started")
            result = mapping.from_impl(
                self._sync(
                    self._impl_obj.wait_for_request(
                        urlOrPredicate=self._wrap_handler(url_or_predicate),
                        timeout=timeout,
                    )
                )
            )
            log_api("<= page.wait_for_request succeded")
            return result
        except Exception as e:
            log_api("<= page.wait_for_request failed")
            raise e

    def wait_for_response(
        self,
        url_or_predicate: typing.Union[
            str, typing.Pattern, typing.Callable[["Response"], bool]
        ],
        timeout: float = None,
    ) -> "Response":
        """Page.wait_for_response

        Returns the matched response.

        Parameters
        ----------
        url_or_predicate : Union[Callable[[Response], bool], Pattern, str]
            Request URL string, regex or predicate receiving `Response` object.
        timeout : Union[float, NoneType]
            Maximum wait time in milliseconds, defaults to 30 seconds, pass `0` to disable the timeout. The default value can be
            changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.

        Returns
        -------
        Response
        """

        try:
            log_api("=> page.wait_for_response started")
            result = mapping.from_impl(
                self._sync(
                    self._impl_obj.wait_for_response(
                        urlOrPredicate=self._wrap_handler(url_or_predicate),
                        timeout=timeout,
                    )
                )
            )
            log_api("<= page.wait_for_response succeded")
            return result
        except Exception as e:
            log_api("<= page.wait_for_response failed")
            raise e

    def wait_for_event(
        self,
        event: str,
        predicate: typing.Union[typing.Callable[[typing.Any], bool]] = None,
        timeout: float = None,
    ) -> typing.Any:
        """Page.wait_for_event

        Returns the event data value.

        Waits for event to fire and passes its value into the predicate function. Returns when the predicate returns truthy
        value. Will throw an error if the page is closed before the event is fired.

        Parameters
        ----------
        event : str
            Event name, same one would pass into `page.on(event)`.
        predicate : Union[Callable[[Any], bool], NoneType]
            receives the event data and resolves to truthy value when the waiting should resolve.
        timeout : Union[float, NoneType]
            maximum time to wait for in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default
            value can be changed by using the `browser_context.set_default_timeout()`.

        Returns
        -------
        Any
        """

        try:
            log_api("=> page.wait_for_event started")
            result = mapping.from_maybe_impl(
                self._sync(
                    self._impl_obj.wait_for_event(
                        event=event,
                        predicate=self._wrap_handler(predicate),
                        timeout=timeout,
                    )
                )
            )
            log_api("<= page.wait_for_event succeded")
            return result
        except Exception as e:
            log_api("<= page.wait_for_event failed")
            raise e

    def go_back(
        self,
        timeout: float = None,
        wait_until: Literal["domcontentloaded", "load", "networkidle"] = None,
    ) -> typing.Union["Response", NoneType]:
        """Page.go_back

        Returns the main resource response. In case of multiple redirects, the navigation will resolve with the response of the
        last redirect. If can not go back, returns `null`.

        Navigate to the previous page in history.

        Parameters
        ----------
        timeout : Union[float, NoneType]
            Maximum operation time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be
            changed by using the `browser_context.set_default_navigation_timeout()`,
            `browser_context.set_default_timeout()`, `page.set_default_navigation_timeout()` or
            `page.set_default_timeout()` methods.
        wait_until : Union["domcontentloaded", "load", "networkidle", NoneType]
            When to consider operation succeeded, defaults to `load`. Events can be either:
            - `'domcontentloaded'` - consider operation to be finished when the `DOMContentLoaded` event is fired.
            - `'load'` - consider operation to be finished when the `load` event is fired.
            - `'networkidle'` - consider operation to be finished when there are no network connections for at least `500` ms.

        Returns
        -------
        Union[Response, NoneType]
        """

        try:
            log_api("=> page.go_back started")
            result = mapping.from_impl_nullable(
                self._sync(
                    self._impl_obj.go_back(timeout=timeout, waitUntil=wait_until)
                )
            )
            log_api("<= page.go_back succeded")
            return result
        except Exception as e:
            log_api("<= page.go_back failed")
            raise e

    def go_forward(
        self,
        timeout: float = None,
        wait_until: Literal["domcontentloaded", "load", "networkidle"] = None,
    ) -> typing.Union["Response", NoneType]:
        """Page.go_forward

        Returns the main resource response. In case of multiple redirects, the navigation will resolve with the response of the
        last redirect. If can not go forward, returns `null`.

        Navigate to the next page in history.

        Parameters
        ----------
        timeout : Union[float, NoneType]
            Maximum operation time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be
            changed by using the `browser_context.set_default_navigation_timeout()`,
            `browser_context.set_default_timeout()`, `page.set_default_navigation_timeout()` or
            `page.set_default_timeout()` methods.
        wait_until : Union["domcontentloaded", "load", "networkidle", NoneType]
            When to consider operation succeeded, defaults to `load`. Events can be either:
            - `'domcontentloaded'` - consider operation to be finished when the `DOMContentLoaded` event is fired.
            - `'load'` - consider operation to be finished when the `load` event is fired.
            - `'networkidle'` - consider operation to be finished when there are no network connections for at least `500` ms.

        Returns
        -------
        Union[Response, NoneType]
        """

        try:
            log_api("=> page.go_forward started")
            result = mapping.from_impl_nullable(
                self._sync(
                    self._impl_obj.go_forward(timeout=timeout, waitUntil=wait_until)
                )
            )
            log_api("<= page.go_forward succeded")
            return result
        except Exception as e:
            log_api("<= page.go_forward failed")
            raise e

    def emulate_media(
        self,
        media: Literal["print", "screen"] = None,
        color_scheme: Literal["dark", "light", "no-preference"] = None,
    ) -> NoneType:
        """Page.emulate_media


        Parameters
        ----------
        media : Union["print", "screen", NoneType]
            Changes the CSS media type of the page. The only allowed values are `'screen'`, `'print'` and `null`. Passing `null`
            disables CSS media emulation. Omitting `media` or passing `undefined` does not change the emulated value. Optional.
        color_scheme : Union["dark", "light", "no-preference", NoneType]
            Emulates `'prefers-colors-scheme'` media feature, supported values are `'light'`, `'dark'`, `'no-preference'`. Passing
            `null` disables color scheme emulation. Omitting `colorScheme` or passing `undefined` does not change the emulated
            value. Optional.
        """

        try:
            log_api("=> page.emulate_media started")
            result = mapping.from_maybe_impl(
                self._sync(
                    self._impl_obj.emulate_media(media=media, colorScheme=color_scheme)
                )
            )
            log_api("<= page.emulate_media succeded")
            return result
        except Exception as e:
            log_api("<= page.emulate_media failed")
            raise e

    def set_viewport_size(self, width: int, height: int) -> NoneType:
        """Page.set_viewport_size

        In the case of multiple pages in a single browser, each page can have its own viewport size. However,
        `browser.new_context()` allows to set viewport size (and more) for all pages in the context at once.

        `page.setViewportSize` will resize the page. A lot of websites don't expect phones to change size, so you should set the
        viewport size before navigating to the page.

        Parameters
        ----------
        width : int
            page width in pixels. **required**
        height : int
            page height in pixels. **required**
        """

        try:
            log_api("=> page.set_viewport_size started")
            result = mapping.from_maybe_impl(
                self._sync(self._impl_obj.set_viewport_size(width=width, height=height))
            )
            log_api("<= page.set_viewport_size succeded")
            return result
        except Exception as e:
            log_api("<= page.set_viewport_size failed")
            raise e

    def viewport_size(self) -> typing.Union[typing.Tuple[int, int], NoneType]:
        """Page.viewport_size

        Returns
        -------
        Union[typing.Tuple[int, int], NoneType]
        """

        try:
            log_api("=> page.viewport_size started")
            result = mapping.from_maybe_impl(self._impl_obj.viewport_size())
            log_api("<= page.viewport_size succeded")
            return result
        except Exception as e:
            log_api("<= page.viewport_size failed")
            raise e

    def bring_to_front(self) -> NoneType:
        """Page.bring_to_front

        Brings page to front (activates tab).
        """

        try:
            log_api("=> page.bring_to_front started")
            result = mapping.from_maybe_impl(
                self._sync(self._impl_obj.bring_to_front())
            )
            log_api("<= page.bring_to_front succeded")
            return result
        except Exception as e:
            log_api("<= page.bring_to_front failed")
            raise e

    def add_init_script(
        self, script: str = None, path: typing.Union[str, pathlib.Path] = None
    ) -> NoneType:
        """Page.add_init_script

        Adds a script which would be evaluated in one of the following scenarios:
        - Whenever the page is navigated.
        - Whenever the child frame is attached or navigated. In this case, the script is evaluated in the context of the newly
          attached frame.

        The script is evaluated after the document was created but before any of its scripts were run. This is useful to amend
        the JavaScript environment, e.g. to seed `Math.random`.

        An example of overriding `Math.random` before the page loads:

        > **NOTE** The order of evaluation of multiple scripts installed via `browser_context.add_init_script()` and
        `page.add_init_script()` is not defined.

        Parameters
        ----------
        script : Union[str, NoneType]
            Script to be evaluated in the page.
        """

        try:
            log_api("=> page.add_init_script started")
            result = mapping.from_maybe_impl(
                self._sync(self._impl_obj.add_init_script(script=script, path=path))
            )
            log_api("<= page.add_init_script succeded")
            return result
        except Exception as e:
            log_api("<= page.add_init_script failed")
            raise e

    def route(
        self,
        url: typing.Union[str, typing.Pattern, typing.Callable[[str], bool]],
        handler: typing.Union[
            typing.Callable[["Route"], typing.Any],
            typing.Callable[["Route", "Request"], typing.Any],
        ],
    ) -> NoneType:
        """Page.route

        Routing provides the capability to modify network requests that are made by a page.

        Once routing is enabled, every request matching the url pattern will stall unless it's continued, fulfilled or aborted.

        > **NOTE** The handler will only be called for the first url if the response is a redirect.

        An example of a naïve handler that aborts all image requests:

        or the same snippet using a regex pattern instead:

        Page routes take precedence over browser context routes (set up with `browser_context.route()`) when request
        matches both handlers.

        > **NOTE** Enabling routing disables http cache.

        Parameters
        ----------
        url : Union[Callable[[str], bool], Pattern, str]
            A glob pattern, regex pattern or predicate receiving [URL] to match while routing.
        handler : Union[Callable[[Route, Request], Any], Callable[[Route], Any]]
            handler function to route the request.
        """

        try:
            log_api("=> page.route started")
            result = mapping.from_maybe_impl(
                self._sync(
                    self._impl_obj.route(
                        url=self._wrap_handler(url), handler=self._wrap_handler(handler)
                    )
                )
            )
            log_api("<= page.route succeded")
            return result
        except Exception as e:
            log_api("<= page.route failed")
            raise e

    def unroute(
        self,
        url: typing.Union[str, typing.Pattern, typing.Callable[[str], bool]],
        handler: typing.Union[
            typing.Callable[["Route"], typing.Any],
            typing.Callable[["Route", "Request"], typing.Any],
        ] = None,
    ) -> NoneType:
        """Page.unroute

        Removes a route created with `page.route()`. When `handler` is not specified, removes all routes for the `url`.

        Parameters
        ----------
        url : Union[Callable[[str], bool], Pattern, str]
            A glob pattern, regex pattern or predicate receiving [URL] to match while routing.
        handler : Union[Callable[[Route, Request], Any], Callable[[Route], Any], NoneType]
            Optional handler function to route the request.
        """

        try:
            log_api("=> page.unroute started")
            result = mapping.from_maybe_impl(
                self._sync(
                    self._impl_obj.unroute(
                        url=self._wrap_handler(url), handler=self._wrap_handler(handler)
                    )
                )
            )
            log_api("<= page.unroute succeded")
            return result
        except Exception as e:
            log_api("<= page.unroute failed")
            raise e

    def screenshot(
        self,
        timeout: float = None,
        type: Literal["jpeg", "png"] = None,
        path: typing.Union[str, pathlib.Path] = None,
        quality: int = None,
        omit_background: bool = None,
        full_page: bool = None,
        clip: "FloatRect" = None,
    ) -> bytes:
        """Page.screenshot

        Returns the buffer with the captured screenshot.

        > **NOTE** Screenshots take at least 1/6 second on Chromium OS X and Chromium Windows. See https://crbug.com/741689 for
        discussion.

        Parameters
        ----------
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        type : Union["jpeg", "png", NoneType]
            Specify screenshot type, defaults to `png`.
        path : Union[pathlib.Path, str, NoneType]
            The file path to save the image to. The screenshot type will be inferred from file extension. If `path` is a relative
            path, then it is resolved relative to the current working directory. If no path is provided, the image won't be saved to
            the disk.
        quality : Union[int, NoneType]
            The quality of the image, between 0-100. Not applicable to `png` images.
        omit_background : Union[bool, NoneType]
            Hides default white background and allows capturing screenshots with transparency. Not applicable to `jpeg` images.
            Defaults to `false`.
        full_page : Union[bool, NoneType]
            When true, takes a screenshot of the full scrollable page, instead of the currently visible viewport. Defaults to
            `false`.
        clip : Union[{x: float, y: float, width: float, height: float}, NoneType]
            An object which specifies clipping of the resulting image. Should have the following fields:

        Returns
        -------
        bytes
        """

        try:
            log_api("=> page.screenshot started")
            result = mapping.from_maybe_impl(
                self._sync(
                    self._impl_obj.screenshot(
                        timeout=timeout,
                        type=type,
                        path=path,
                        quality=quality,
                        omitBackground=omit_background,
                        fullPage=full_page,
                        clip=clip,
                    )
                )
            )
            log_api("<= page.screenshot succeded")
            return result
        except Exception as e:
            log_api("<= page.screenshot failed")
            raise e

    def title(self) -> str:
        """Page.title

        Returns the page's title. Shortcut for main frame's `frame.title()`.

        Returns
        -------
        str
        """

        try:
            log_api("=> page.title started")
            result = mapping.from_maybe_impl(self._sync(self._impl_obj.title()))
            log_api("<= page.title succeded")
            return result
        except Exception as e:
            log_api("<= page.title failed")
            raise e

    def close(self, run_before_unload: bool = None) -> NoneType:
        """Page.close

        If `runBeforeUnload` is `false`, does not run any unload handlers and waits for the page to be closed. If
        `runBeforeUnload` is `true` the method will run unload handlers, but will **not** wait for the page to close.

        By default, `page.close()` **does not** run `beforeunload` handlers.

        > **NOTE** if `runBeforeUnload` is passed as true, a `beforeunload` dialog might be summoned
        > and should be handled manually via [`event: Page.dialog`] event.

        Parameters
        ----------
        run_before_unload : Union[bool, NoneType]
            Defaults to `false`. Whether to run the
            [before unload](https://developer.mozilla.org/en-US/docs/Web/Events/beforeunload) page handlers.
        """

        try:
            log_api("=> page.close started")
            result = mapping.from_maybe_impl(
                self._sync(self._impl_obj.close(runBeforeUnload=run_before_unload))
            )
            log_api("<= page.close succeded")
            return result
        except Exception as e:
            log_api("<= page.close failed")
            raise e

    def is_closed(self) -> bool:
        """Page.is_closed

        Indicates that the page has been closed.

        Returns
        -------
        bool
        """

        try:
            log_api("=> page.is_closed started")
            result = mapping.from_maybe_impl(self._impl_obj.is_closed())
            log_api("<= page.is_closed succeded")
            return result
        except Exception as e:
            log_api("<= page.is_closed failed")
            raise e

    def click(
        self,
        selector: str,
        modifiers: typing.Union[
            typing.List[Literal["Alt", "Control", "Meta", "Shift"]]
        ] = None,
        position: typing.Union[typing.Tuple[float, float]] = None,
        delay: float = None,
        button: Literal["left", "middle", "right"] = None,
        click_count: int = None,
        timeout: float = None,
        force: bool = None,
        no_wait_after: bool = None,
    ) -> NoneType:
        """Page.click

        This method clicks an element matching `selector` by performing the following steps:
        1. Find an element match matching `selector`. If there is none, wait until a matching element is attached to the DOM.
        1. Wait for [actionability](./actionability.md) checks on the matched element, unless `force` option is set. If the
           element is detached during the checks, the whole action is retried.
        1. Scroll the element into view if needed.
        1. Use `page.mouse` to click in the center of the element, or the specified `position`.
        1. Wait for initiated navigations to either succeed or fail, unless `noWaitAfter` option is set.

        When all steps combined have not finished during the specified `timeout`, this method rejects with a `TimeoutError`.
        Passing zero timeout disables this.

        Shortcut for main frame's `frame.click()`.

        Parameters
        ----------
        selector : str
            A selector to search for element. If there are multiple elements satisfying the selector, the first will be used. See
            [working with selectors](./selectors.md#working-with-selectors) for more details.
        modifiers : Union[List[Union["Alt", "Control", "Meta", "Shift"]], NoneType]
            Modifier keys to press. Ensures that only these modifiers are pressed during the operation, and then restores current
            modifiers back. If not specified, currently pressed modifiers are used.
        position : Union[typing.Tuple[float, float], NoneType]
            A point to use relative to the top-left corner of element padding box. If not specified, uses some visible point of the
            element.
        delay : Union[float, NoneType]
            Time to wait between `mousedown` and `mouseup` in milliseconds. Defaults to 0.
        button : Union["left", "middle", "right", NoneType]
            Defaults to `left`.
        click_count : Union[int, NoneType]
            defaults to 1. See [UIEvent.detail].
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        force : Union[bool, NoneType]
            Whether to bypass the [actionability](./actionability.md) checks. Defaults to `false`.
        no_wait_after : Union[bool, NoneType]
            Actions that initiate navigations are waiting for these navigations to happen and for pages to start loading. You can
            opt out of waiting via setting this flag. You would only need this option in the exceptional cases such as navigating to
            inaccessible pages. Defaults to `false`.
        """

        try:
            log_api("=> page.click started")
            result = mapping.from_maybe_impl(
                self._sync(
                    self._impl_obj.click(
                        selector=selector,
                        modifiers=modifiers,
                        position=position,
                        delay=delay,
                        button=button,
                        clickCount=click_count,
                        timeout=timeout,
                        force=force,
                        noWaitAfter=no_wait_after,
                    )
                )
            )
            log_api("<= page.click succeded")
            return result
        except Exception as e:
            log_api("<= page.click failed")
            raise e

    def dblclick(
        self,
        selector: str,
        modifiers: typing.Union[
            typing.List[Literal["Alt", "Control", "Meta", "Shift"]]
        ] = None,
        position: typing.Union[typing.Tuple[float, float]] = None,
        delay: float = None,
        button: Literal["left", "middle", "right"] = None,
        timeout: float = None,
        force: bool = None,
        no_wait_after: bool = None,
    ) -> NoneType:
        """Page.dblclick

        This method double clicks an element matching `selector` by performing the following steps:
        1. Find an element match matching `selector`. If there is none, wait until a matching element is attached to the DOM.
        1. Wait for [actionability](./actionability.md) checks on the matched element, unless `force` option is set. If the
           element is detached during the checks, the whole action is retried.
        1. Scroll the element into view if needed.
        1. Use `page.mouse` to double click in the center of the element, or the specified `position`.
        1. Wait for initiated navigations to either succeed or fail, unless `noWaitAfter` option is set. Note that if the
           first click of the `dblclick()` triggers a navigation event, this method will reject.

        When all steps combined have not finished during the specified `timeout`, this method rejects with a `TimeoutError`.
        Passing zero timeout disables this.

        > **NOTE** `page.dblclick()` dispatches two `click` events and a single `dblclick` event.

        Shortcut for main frame's `frame.dblclick()`.

        Parameters
        ----------
        selector : str
            A selector to search for element. If there are multiple elements satisfying the selector, the first will be used. See
            [working with selectors](./selectors.md#working-with-selectors) for more details.
        modifiers : Union[List[Union["Alt", "Control", "Meta", "Shift"]], NoneType]
            Modifier keys to press. Ensures that only these modifiers are pressed during the operation, and then restores current
            modifiers back. If not specified, currently pressed modifiers are used.
        position : Union[typing.Tuple[float, float], NoneType]
            A point to use relative to the top-left corner of element padding box. If not specified, uses some visible point of the
            element.
        delay : Union[float, NoneType]
            Time to wait between `mousedown` and `mouseup` in milliseconds. Defaults to 0.
        button : Union["left", "middle", "right", NoneType]
            Defaults to `left`.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        force : Union[bool, NoneType]
            Whether to bypass the [actionability](./actionability.md) checks. Defaults to `false`.
        no_wait_after : Union[bool, NoneType]
            Actions that initiate navigations are waiting for these navigations to happen and for pages to start loading. You can
            opt out of waiting via setting this flag. You would only need this option in the exceptional cases such as navigating to
            inaccessible pages. Defaults to `false`.
        """

        try:
            log_api("=> page.dblclick started")
            result = mapping.from_maybe_impl(
                self._sync(
                    self._impl_obj.dblclick(
                        selector=selector,
                        modifiers=modifiers,
                        position=position,
                        delay=delay,
                        button=button,
                        timeout=timeout,
                        force=force,
                        noWaitAfter=no_wait_after,
                    )
                )
            )
            log_api("<= page.dblclick succeded")
            return result
        except Exception as e:
            log_api("<= page.dblclick failed")
            raise e

    def tap(
        self,
        selector: str,
        modifiers: typing.Union[
            typing.List[Literal["Alt", "Control", "Meta", "Shift"]]
        ] = None,
        position: typing.Union[typing.Tuple[float, float]] = None,
        timeout: float = None,
        force: bool = None,
        no_wait_after: bool = None,
    ) -> NoneType:
        """Page.tap

        This method taps an element matching `selector` by performing the following steps:
        1. Find an element match matching `selector`. If there is none, wait until a matching element is attached to the DOM.
        1. Wait for [actionability](./actionability.md) checks on the matched element, unless `force` option is set. If the
           element is detached during the checks, the whole action is retried.
        1. Scroll the element into view if needed.
        1. Use `page.touchscreen` to tap the center of the element, or the specified `position`.
        1. Wait for initiated navigations to either succeed or fail, unless `noWaitAfter` option is set.

        When all steps combined have not finished during the specified `timeout`, this method rejects with a `TimeoutError`.
        Passing zero timeout disables this.

        > **NOTE** `page.tap()` requires that the `hasTouch` option of the browser context be set to true.

        Shortcut for main frame's `frame.tap()`.

        Parameters
        ----------
        selector : str
            A selector to search for element. If there are multiple elements satisfying the selector, the first will be used. See
            [working with selectors](./selectors.md#working-with-selectors) for more details.
        modifiers : Union[List[Union["Alt", "Control", "Meta", "Shift"]], NoneType]
            Modifier keys to press. Ensures that only these modifiers are pressed during the operation, and then restores current
            modifiers back. If not specified, currently pressed modifiers are used.
        position : Union[typing.Tuple[float, float], NoneType]
            A point to use relative to the top-left corner of element padding box. If not specified, uses some visible point of the
            element.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        force : Union[bool, NoneType]
            Whether to bypass the [actionability](./actionability.md) checks. Defaults to `false`.
        no_wait_after : Union[bool, NoneType]
            Actions that initiate navigations are waiting for these navigations to happen and for pages to start loading. You can
            opt out of waiting via setting this flag. You would only need this option in the exceptional cases such as navigating to
            inaccessible pages. Defaults to `false`.
        """

        try:
            log_api("=> page.tap started")
            result = mapping.from_maybe_impl(
                self._sync(
                    self._impl_obj.tap(
                        selector=selector,
                        modifiers=modifiers,
                        position=position,
                        timeout=timeout,
                        force=force,
                        noWaitAfter=no_wait_after,
                    )
                )
            )
            log_api("<= page.tap succeded")
            return result
        except Exception as e:
            log_api("<= page.tap failed")
            raise e

    def fill(
        self,
        selector: str,
        value: str,
        timeout: float = None,
        no_wait_after: bool = None,
    ) -> NoneType:
        """Page.fill

        This method waits for an element matching `selector`, waits for [actionability](./actionability.md) checks, focuses the
        element, fills it and triggers an `input` event after filling. If the element matching `selector` is not an `<input>`,
        `<textarea>` or `[contenteditable]` element, this method throws an error. Note that you can pass an empty string to
        clear the input field.

        To send fine-grained keyboard events, use `page.type()`.

        Shortcut for main frame's `frame.fill()`

        Parameters
        ----------
        selector : str
            A selector to search for element. If there are multiple elements satisfying the selector, the first will be used. See
            [working with selectors](./selectors.md#working-with-selectors) for more details.
        value : str
            Value to fill for the `<input>`, `<textarea>` or `[contenteditable]` element.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        no_wait_after : Union[bool, NoneType]
            Actions that initiate navigations are waiting for these navigations to happen and for pages to start loading. You can
            opt out of waiting via setting this flag. You would only need this option in the exceptional cases such as navigating to
            inaccessible pages. Defaults to `false`.
        """

        try:
            log_api("=> page.fill started")
            result = mapping.from_maybe_impl(
                self._sync(
                    self._impl_obj.fill(
                        selector=selector,
                        value=value,
                        timeout=timeout,
                        noWaitAfter=no_wait_after,
                    )
                )
            )
            log_api("<= page.fill succeded")
            return result
        except Exception as e:
            log_api("<= page.fill failed")
            raise e

    def focus(self, selector: str, timeout: float = None) -> NoneType:
        """Page.focus

        This method fetches an element with `selector` and focuses it. If there's no element matching `selector`, the method
        waits until a matching element appears in the DOM.

        Shortcut for main frame's `frame.focus()`.

        Parameters
        ----------
        selector : str
            A selector to search for element. If there are multiple elements satisfying the selector, the first will be used. See
            [working with selectors](./selectors.md#working-with-selectors) for more details.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        """

        try:
            log_api("=> page.focus started")
            result = mapping.from_maybe_impl(
                self._sync(self._impl_obj.focus(selector=selector, timeout=timeout))
            )
            log_api("<= page.focus succeded")
            return result
        except Exception as e:
            log_api("<= page.focus failed")
            raise e

    def text_content(
        self, selector: str, timeout: float = None
    ) -> typing.Union[str, NoneType]:
        """Page.text_content

        Returns `element.textContent`.

        Parameters
        ----------
        selector : str
            A selector to search for element. If there are multiple elements satisfying the selector, the first will be used. See
            [working with selectors](./selectors.md#working-with-selectors) for more details.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.

        Returns
        -------
        Union[str, NoneType]
        """

        try:
            log_api("=> page.text_content started")
            result = mapping.from_maybe_impl(
                self._sync(
                    self._impl_obj.text_content(selector=selector, timeout=timeout)
                )
            )
            log_api("<= page.text_content succeded")
            return result
        except Exception as e:
            log_api("<= page.text_content failed")
            raise e

    def inner_text(self, selector: str, timeout: float = None) -> str:
        """Page.inner_text

        Returns `element.innerText`.

        Parameters
        ----------
        selector : str
            A selector to search for element. If there are multiple elements satisfying the selector, the first will be used. See
            [working with selectors](./selectors.md#working-with-selectors) for more details.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.

        Returns
        -------
        str
        """

        try:
            log_api("=> page.inner_text started")
            result = mapping.from_maybe_impl(
                self._sync(
                    self._impl_obj.inner_text(selector=selector, timeout=timeout)
                )
            )
            log_api("<= page.inner_text succeded")
            return result
        except Exception as e:
            log_api("<= page.inner_text failed")
            raise e

    def inner_html(self, selector: str, timeout: float = None) -> str:
        """Page.inner_html

        Returns `element.innerHTML`.

        Parameters
        ----------
        selector : str
            A selector to search for element. If there are multiple elements satisfying the selector, the first will be used. See
            [working with selectors](./selectors.md#working-with-selectors) for more details.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.

        Returns
        -------
        str
        """

        try:
            log_api("=> page.inner_html started")
            result = mapping.from_maybe_impl(
                self._sync(
                    self._impl_obj.inner_html(selector=selector, timeout=timeout)
                )
            )
            log_api("<= page.inner_html succeded")
            return result
        except Exception as e:
            log_api("<= page.inner_html failed")
            raise e

    def get_attribute(
        self, selector: str, name: str, timeout: float = None
    ) -> typing.Union[str, NoneType]:
        """Page.get_attribute

        Returns element attribute value.

        Parameters
        ----------
        selector : str
            A selector to search for element. If there are multiple elements satisfying the selector, the first will be used. See
            [working with selectors](./selectors.md#working-with-selectors) for more details.
        name : str
            Attribute name to get the value for.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.

        Returns
        -------
        Union[str, NoneType]
        """

        try:
            log_api("=> page.get_attribute started")
            result = mapping.from_maybe_impl(
                self._sync(
                    self._impl_obj.get_attribute(
                        selector=selector, name=name, timeout=timeout
                    )
                )
            )
            log_api("<= page.get_attribute succeded")
            return result
        except Exception as e:
            log_api("<= page.get_attribute failed")
            raise e

    def hover(
        self,
        selector: str,
        modifiers: typing.Union[
            typing.List[Literal["Alt", "Control", "Meta", "Shift"]]
        ] = None,
        position: typing.Union[typing.Tuple[float, float]] = None,
        timeout: float = None,
        force: bool = None,
    ) -> NoneType:
        """Page.hover

        This method hovers over an element matching `selector` by performing the following steps:
        1. Find an element match matching `selector`. If there is none, wait until a matching element is attached to the DOM.
        1. Wait for [actionability](./actionability.md) checks on the matched element, unless `force` option is set. If the
           element is detached during the checks, the whole action is retried.
        1. Scroll the element into view if needed.
        1. Use `page.mouse` to hover over the center of the element, or the specified `position`.
        1. Wait for initiated navigations to either succeed or fail, unless `noWaitAfter` option is set.

        When all steps combined have not finished during the specified `timeout`, this method rejects with a `TimeoutError`.
        Passing zero timeout disables this.

        Shortcut for main frame's `frame.hover()`.

        Parameters
        ----------
        selector : str
            A selector to search for element. If there are multiple elements satisfying the selector, the first will be used. See
            [working with selectors](./selectors.md#working-with-selectors) for more details.
        modifiers : Union[List[Union["Alt", "Control", "Meta", "Shift"]], NoneType]
            Modifier keys to press. Ensures that only these modifiers are pressed during the operation, and then restores current
            modifiers back. If not specified, currently pressed modifiers are used.
        position : Union[typing.Tuple[float, float], NoneType]
            A point to use relative to the top-left corner of element padding box. If not specified, uses some visible point of the
            element.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        force : Union[bool, NoneType]
            Whether to bypass the [actionability](./actionability.md) checks. Defaults to `false`.
        """

        try:
            log_api("=> page.hover started")
            result = mapping.from_maybe_impl(
                self._sync(
                    self._impl_obj.hover(
                        selector=selector,
                        modifiers=modifiers,
                        position=position,
                        timeout=timeout,
                        force=force,
                    )
                )
            )
            log_api("<= page.hover succeded")
            return result
        except Exception as e:
            log_api("<= page.hover failed")
            raise e

    def select_option(
        self,
        selector: str,
        value: typing.Union[str, typing.List[str]] = None,
        index: typing.Union[int, typing.List[int]] = None,
        label: typing.Union[str, typing.List[str]] = None,
        element: typing.Union["ElementHandle", typing.List["ElementHandle"]] = None,
        timeout: float = None,
        no_wait_after: bool = None,
    ) -> typing.List[str]:
        """Page.select_option

        Returns the array of option values that have been successfully selected.

        Triggers a `change` and `input` event once all the provided options have been selected. If there's no `<select>` element
        matching `selector`, the method throws an error.

        Shortcut for main frame's `frame.select_option()`

        Parameters
        ----------
        selector : str
            A selector to search for element. If there are multiple elements satisfying the selector, the first will be used. See
            [working with selectors](./selectors.md#working-with-selectors) for more details.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        no_wait_after : Union[bool, NoneType]
            Actions that initiate navigations are waiting for these navigations to happen and for pages to start loading. You can
            opt out of waiting via setting this flag. You would only need this option in the exceptional cases such as navigating to
            inaccessible pages. Defaults to `false`.

        Returns
        -------
        List[str]
        """

        try:
            log_api("=> page.select_option started")
            result = mapping.from_maybe_impl(
                self._sync(
                    self._impl_obj.select_option(
                        selector=selector,
                        value=value,
                        index=index,
                        label=label,
                        element=mapping.to_impl(element),
                        timeout=timeout,
                        noWaitAfter=no_wait_after,
                    )
                )
            )
            log_api("<= page.select_option succeded")
            return result
        except Exception as e:
            log_api("<= page.select_option failed")
            raise e

    def set_input_files(
        self,
        selector: str,
        files: typing.Union[
            str, "FilePayload", typing.List[str], typing.List["FilePayload"]
        ],
        timeout: float = None,
        no_wait_after: bool = None,
    ) -> NoneType:
        """Page.set_input_files

        This method expects `selector` to point to an
        [input element](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input).

        Sets the value of the file input to these file paths or files. If some of the `filePaths` are relative paths, then they
        are resolved relative to the the current working directory. For empty array, clears the selected files.

        Parameters
        ----------
        selector : str
            A selector to search for element. If there are multiple elements satisfying the selector, the first will be used. See
            [working with selectors](./selectors.md#working-with-selectors) for more details.
        files : Union[List[str], List[{name: str, mime_type: str, buffer: bytes}], str, {name: str, mime_type: str, buffer: bytes}]
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        no_wait_after : Union[bool, NoneType]
            Actions that initiate navigations are waiting for these navigations to happen and for pages to start loading. You can
            opt out of waiting via setting this flag. You would only need this option in the exceptional cases such as navigating to
            inaccessible pages. Defaults to `false`.
        """

        try:
            log_api("=> page.set_input_files started")
            result = mapping.from_maybe_impl(
                self._sync(
                    self._impl_obj.set_input_files(
                        selector=selector,
                        files=files,
                        timeout=timeout,
                        noWaitAfter=no_wait_after,
                    )
                )
            )
            log_api("<= page.set_input_files succeded")
            return result
        except Exception as e:
            log_api("<= page.set_input_files failed")
            raise e

    def type(
        self,
        selector: str,
        text: str,
        delay: float = None,
        timeout: float = None,
        no_wait_after: bool = None,
    ) -> NoneType:
        """Page.type

        Sends a `keydown`, `keypress`/`input`, and `keyup` event for each character in the text. `page.type` can be used to send
        fine-grained keyboard events. To fill values in form fields, use `page.fill()`.

        To press a special key, like `Control` or `ArrowDown`, use `keyboard.press()`.

        Shortcut for main frame's `frame.type()`.

        Parameters
        ----------
        selector : str
            A selector to search for element. If there are multiple elements satisfying the selector, the first will be used. See
            [working with selectors](./selectors.md#working-with-selectors) for more details.
        text : str
            A text to type into a focused element.
        delay : Union[float, NoneType]
            Time to wait between key presses in milliseconds. Defaults to 0.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        no_wait_after : Union[bool, NoneType]
            Actions that initiate navigations are waiting for these navigations to happen and for pages to start loading. You can
            opt out of waiting via setting this flag. You would only need this option in the exceptional cases such as navigating to
            inaccessible pages. Defaults to `false`.
        """

        try:
            log_api("=> page.type started")
            result = mapping.from_maybe_impl(
                self._sync(
                    self._impl_obj.type(
                        selector=selector,
                        text=text,
                        delay=delay,
                        timeout=timeout,
                        noWaitAfter=no_wait_after,
                    )
                )
            )
            log_api("<= page.type succeded")
            return result
        except Exception as e:
            log_api("<= page.type failed")
            raise e

    def press(
        self,
        selector: str,
        key: str,
        delay: float = None,
        timeout: float = None,
        no_wait_after: bool = None,
    ) -> NoneType:
        """Page.press

        Focuses the element, and then uses `keyboard.down()` and `keyboard.up()`.

        `key` can specify the intended [keyboardEvent.key](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/key)
        value or a single character to generate the text for. A superset of the `key` values can be found
        [here](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/key/Key_Values). Examples of the keys are:

        `F1` - `F12`, `Digit0`- `Digit9`, `KeyA`- `KeyZ`, `Backquote`, `Minus`, `Equal`, `Backslash`, `Backspace`, `Tab`,
        `Delete`, `Escape`, `ArrowDown`, `End`, `Enter`, `Home`, `Insert`, `PageDown`, `PageUp`, `ArrowRight`, `ArrowUp`, etc.

        Following modification shortcuts are also supported: `Shift`, `Control`, `Alt`, `Meta`, `ShiftLeft`.

        Holding down `Shift` will type the text that corresponds to the `key` in the upper case.

        If `key` is a single character, it is case-sensitive, so the values `a` and `A` will generate different respective
        texts.

        Shortcuts such as `key: "Control+o"` or `key: "Control+Shift+T"` are supported as well. When speficied with the
        modifier, modifier is pressed and being held while the subsequent key is being pressed.

        Parameters
        ----------
        selector : str
            A selector to search for element. If there are multiple elements satisfying the selector, the first will be used. See
            [working with selectors](./selectors.md#working-with-selectors) for more details.
        key : str
            Name of the key to press or a character to generate, such as `ArrowLeft` or `a`.
        delay : Union[float, NoneType]
            Time to wait between `keydown` and `keyup` in milliseconds. Defaults to 0.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        no_wait_after : Union[bool, NoneType]
            Actions that initiate navigations are waiting for these navigations to happen and for pages to start loading. You can
            opt out of waiting via setting this flag. You would only need this option in the exceptional cases such as navigating to
            inaccessible pages. Defaults to `false`.
        """

        try:
            log_api("=> page.press started")
            result = mapping.from_maybe_impl(
                self._sync(
                    self._impl_obj.press(
                        selector=selector,
                        key=key,
                        delay=delay,
                        timeout=timeout,
                        noWaitAfter=no_wait_after,
                    )
                )
            )
            log_api("<= page.press succeded")
            return result
        except Exception as e:
            log_api("<= page.press failed")
            raise e

    def check(
        self,
        selector: str,
        timeout: float = None,
        force: bool = None,
        no_wait_after: bool = None,
    ) -> NoneType:
        """Page.check

        This method checks an element matching `selector` by performing the following steps:
        1. Find an element match matching `selector`. If there is none, wait until a matching element is attached to the DOM.
        1. Ensure that matched element is a checkbox or a radio input. If not, this method rejects. If the element is already
           checked, this method returns immediately.
        1. Wait for [actionability](./actionability.md) checks on the matched element, unless `force` option is set. If the
           element is detached during the checks, the whole action is retried.
        1. Scroll the element into view if needed.
        1. Use `page.mouse` to click in the center of the element.
        1. Wait for initiated navigations to either succeed or fail, unless `noWaitAfter` option is set.
        1. Ensure that the element is now checked. If not, this method rejects.

        When all steps combined have not finished during the specified `timeout`, this method rejects with a `TimeoutError`.
        Passing zero timeout disables this.

        Shortcut for main frame's `frame.check()`.

        Parameters
        ----------
        selector : str
            A selector to search for element. If there are multiple elements satisfying the selector, the first will be used. See
            [working with selectors](./selectors.md#working-with-selectors) for more details.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        force : Union[bool, NoneType]
            Whether to bypass the [actionability](./actionability.md) checks. Defaults to `false`.
        no_wait_after : Union[bool, NoneType]
            Actions that initiate navigations are waiting for these navigations to happen and for pages to start loading. You can
            opt out of waiting via setting this flag. You would only need this option in the exceptional cases such as navigating to
            inaccessible pages. Defaults to `false`.
        """

        try:
            log_api("=> page.check started")
            result = mapping.from_maybe_impl(
                self._sync(
                    self._impl_obj.check(
                        selector=selector,
                        timeout=timeout,
                        force=force,
                        noWaitAfter=no_wait_after,
                    )
                )
            )
            log_api("<= page.check succeded")
            return result
        except Exception as e:
            log_api("<= page.check failed")
            raise e

    def uncheck(
        self,
        selector: str,
        timeout: float = None,
        force: bool = None,
        no_wait_after: bool = None,
    ) -> NoneType:
        """Page.uncheck

        This method unchecks an element matching `selector` by performing the following steps:
        1. Find an element match matching `selector`. If there is none, wait until a matching element is attached to the DOM.
        1. Ensure that matched element is a checkbox or a radio input. If not, this method rejects. If the element is already
           unchecked, this method returns immediately.
        1. Wait for [actionability](./actionability.md) checks on the matched element, unless `force` option is set. If the
           element is detached during the checks, the whole action is retried.
        1. Scroll the element into view if needed.
        1. Use `page.mouse` to click in the center of the element.
        1. Wait for initiated navigations to either succeed or fail, unless `noWaitAfter` option is set.
        1. Ensure that the element is now unchecked. If not, this method rejects.

        When all steps combined have not finished during the specified `timeout`, this method rejects with a `TimeoutError`.
        Passing zero timeout disables this.

        Shortcut for main frame's `frame.uncheck()`.

        Parameters
        ----------
        selector : str
            A selector to search for element. If there are multiple elements satisfying the selector, the first will be used. See
            [working with selectors](./selectors.md#working-with-selectors) for more details.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by
            using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods.
        force : Union[bool, NoneType]
            Whether to bypass the [actionability](./actionability.md) checks. Defaults to `false`.
        no_wait_after : Union[bool, NoneType]
            Actions that initiate navigations are waiting for these navigations to happen and for pages to start loading. You can
            opt out of waiting via setting this flag. You would only need this option in the exceptional cases such as navigating to
            inaccessible pages. Defaults to `false`.
        """

        try:
            log_api("=> page.uncheck started")
            result = mapping.from_maybe_impl(
                self._sync(
                    self._impl_obj.uncheck(
                        selector=selector,
                        timeout=timeout,
                        force=force,
                        noWaitAfter=no_wait_after,
                    )
                )
            )
            log_api("<= page.uncheck succeded")
            return result
        except Exception as e:
            log_api("<= page.uncheck failed")
            raise e

    def wait_for_timeout(self, timeout: float) -> NoneType:
        """Page.wait_for_timeout

        Waits for the given `timeout` in milliseconds.

        Note that `page.waitForTimeout()` should only be used for debugging. Tests using the timer in production are going to be
        flaky. Use signals such as network events, selectors becoming visible and others instead.

        Shortcut for main frame's `frame.wait_for_timeout()`.

        Parameters
        ----------
        timeout : float
            A timeout to wait for
        """

        try:
            log_api("=> page.wait_for_timeout started")
            result = mapping.from_maybe_impl(
                self._sync(self._impl_obj.wait_for_timeout(timeout=timeout))
            )
            log_api("<= page.wait_for_timeout succeded")
            return result
        except Exception as e:
            log_api("<= page.wait_for_timeout failed")
            raise e

    def wait_for_function(
        self,
        expression: str,
        arg: typing.Any = None,
        force_expr: bool = None,
        timeout: float = None,
        polling: typing.Union[float, Literal["raf"]] = None,
    ) -> "JSHandle":
        """Page.wait_for_function

        Returns when the `pageFunction` returns a truthy value. It resolves to a JSHandle of the truthy value.

        The `waitForFunction` can be used to observe viewport size change:

        To pass an argument to the predicate of `page.waitForFunction` function:

        Shortcut for main frame's `frame.wait_for_function()`.

        Parameters
        ----------
        expression : str
            Function to be evaluated in browser context
        force_expr : bool
            Whether to treat given expression as JavaScript evaluate expression, even though it looks like an arrow function
        arg : Union[Any, NoneType]
            Optional argument to pass to `pageFunction`
        timeout : Union[float, NoneType]
            maximum time to wait for in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default
            value can be changed by using the `browser_context.set_default_timeout()`.
        polling : Union["raf", float, NoneType]
            If `polling` is `'raf'`, then `pageFunction` is constantly executed in `requestAnimationFrame` callback. If `polling` is
            a number, then it is treated as an interval in milliseconds at which the function would be executed. Defaults to `raf`.

        Returns
        -------
        JSHandle
        """

        try:
            log_api("=> page.wait_for_function started")
            result = mapping.from_impl(
                self._sync(
                    self._impl_obj.wait_for_function(
                        expression=expression,
                        arg=mapping.to_impl(arg),
                        force_expr=force_expr,
                        timeout=timeout,
                        polling=polling,
                    )
                )
            )
            log_api("<= page.wait_for_function succeded")
            return result
        except Exception as e:
            log_api("<= page.wait_for_function failed")
            raise e

    def pdf(
        self,
        scale: float = None,
        display_header_footer: bool = None,
        header_template: str = None,
        footer_template: str = None,
        print_background: bool = None,
        landscape: bool = None,
        page_ranges: str = None,
        format: str = None,
        width: typing.Union[str, float] = None,
        height: typing.Union[str, float] = None,
        prefer_css_page_size: bool = None,
        margin: "PdfMargins" = None,
        path: typing.Union[str, pathlib.Path] = None,
    ) -> bytes:
        """Page.pdf

        Returns the PDF buffer.

        > **NOTE** Generating a pdf is currently only supported in Chromium headless.

        `page.pdf()` generates a pdf of the page with `print` css media. To generate a pdf with `screen` media, call
        `page.emulate_media()` before calling `page.pdf()`:

        > **NOTE** By default, `page.pdf()` generates a pdf with modified colors for printing. Use the
        [`-webkit-print-color-adjust`](https://developer.mozilla.org/en-US/docs/Web/CSS/-webkit-print-color-adjust) property to
        force rendering of exact colors.

        The `width`, `height`, and `margin` options accept values labeled with units. Unlabeled values are treated as pixels.

        A few examples:
        - `page.pdf({width: 100})` - prints with width set to 100 pixels
        - `page.pdf({width: '100px'})` - prints with width set to 100 pixels
        - `page.pdf({width: '10cm'})` - prints with width set to 10 centimeters.

        All possible units are:
        - `px` - pixel
        - `in` - inch
        - `cm` - centimeter
        - `mm` - millimeter

        The `format` options are:
        - `Letter`: 8.5in x 11in
        - `Legal`: 8.5in x 14in
        - `Tabloid`: 11in x 17in
        - `Ledger`: 17in x 11in
        - `A0`: 33.1in x 46.8in
        - `A1`: 23.4in x 33.1in
        - `A2`: 16.54in x 23.4in
        - `A3`: 11.7in x 16.54in
        - `A4`: 8.27in x 11.7in
        - `A5`: 5.83in x 8.27in
        - `A6`: 4.13in x 5.83in

        > **NOTE** `headerTemplate` and `footerTemplate` markup have the following limitations:
        > 1. Script tags inside templates are not evaluated.
        > 2. Page styles are not visible inside templates.

        Parameters
        ----------
        scale : Union[float, NoneType]
            Scale of the webpage rendering. Defaults to `1`. Scale amount must be between 0.1 and 2.
        display_header_footer : Union[bool, NoneType]
            Display header and footer. Defaults to `false`.
        header_template : Union[str, NoneType]
            HTML template for the print header. Should be valid HTML markup with following classes used to inject printing values
            into them:
            - `'date'` formatted print date
            - `'title'` document title
            - `'url'` document location
            - `'pageNumber'` current page number
            - `'totalPages'` total pages in the document
        footer_template : Union[str, NoneType]
            HTML template for the print footer. Should use the same format as the `headerTemplate`.
        print_background : Union[bool, NoneType]
            Print background graphics. Defaults to `false`.
        landscape : Union[bool, NoneType]
            Paper orientation. Defaults to `false`.
        page_ranges : Union[str, NoneType]
            Paper ranges to print, e.g., '1-5, 8, 11-13'. Defaults to the empty string, which means print all pages.
        format : Union[str, NoneType]
            Paper format. If set, takes priority over `width` or `height` options. Defaults to 'Letter'.
        width : Union[float, str, NoneType]
            Paper width, accepts values labeled with units.
        height : Union[float, str, NoneType]
            Paper height, accepts values labeled with units.
        prefer_css_page_size : Union[bool, NoneType]
            Give any CSS `@page` size declared in the page priority over what is declared in `width` and `height` or `format`
            options. Defaults to `false`, which will scale the content to fit the paper size.
        margin : Union[{top: Union[float, str, NoneType], right: Union[float, str, NoneType], bottom: Union[float, str, NoneType], left: Union[float, str, NoneType]}, NoneType]
            Paper margins, defaults to none.
        path : Union[pathlib.Path, str, NoneType]
            The file path to save the PDF to. If `path` is a relative path, then it is resolved relative to the current working
            directory. If no path is provided, the PDF won't be saved to the disk.

        Returns
        -------
        bytes
        """

        try:
            log_api("=> page.pdf started")
            result = mapping.from_maybe_impl(
                self._sync(
                    self._impl_obj.pdf(
                        scale=scale,
                        displayHeaderFooter=display_header_footer,
                        headerTemplate=header_template,
                        footerTemplate=footer_template,
                        printBackground=print_background,
                        landscape=landscape,
                        pageRanges=page_ranges,
                        format=format,
                        width=width,
                        height=height,
                        preferCSSPageSize=prefer_css_page_size,
                        margin=margin,
                        path=path,
                    )
                )
            )
            log_api("<= page.pdf succeded")
            return result
        except Exception as e:
            log_api("<= page.pdf failed")
            raise e

    def expect_event(
        self,
        event: str,
        predicate: typing.Union[typing.Callable[[typing.Any], bool]] = None,
        timeout: float = None,
    ) -> EventContextManager:
        """Page.expect_event

        Returns context manager that waits for ``event`` to fire upon exit. It passes event's value
        into the ``predicate`` function and waits for the predicate to return a truthy value. Will throw
        an error if the page is closed before the ``event`` is fired.

        with page.expect_event() as event_info:
            page.click("button")
        value = event_info.value

        Parameters
        ----------
        predicate : Optional[typing.Callable[[Any], bool]]
            Predicate receiving event data.
        timeout : Optional[int]
            Maximum wait time in milliseconds, defaults to 30 seconds, pass `0` to disable the timeout.
            The default value can be changed by using the browserContext.set_default_timeout(timeout) or
            page.set_default_timeout(timeout) methods.
        """
        return EventContextManager(
            self, self._impl_obj.wait_for_event(event, predicate, timeout)
        )

    def expect_console_message(
        self,
        predicate: typing.Union[typing.Callable[["ConsoleMessage"], bool]] = None,
        timeout: float = None,
    ) -> EventContextManager["ConsoleMessage"]:
        """Page.expect_console_message

        Returns context manager that waits for ``event`` to fire upon exit. It passes event's value
        into the ``predicate`` function and waits for the predicate to return a truthy value. Will throw
        an error if the page is closed before the ``event`` is fired.

        with page.expect_console() as event_info:
            page.click("button")
        value = event_info.value

        Parameters
        ----------
        predicate : Optional[typing.Callable[[Any], bool]]
            Predicate receiving event data.
        timeout : Optional[int]
            Maximum wait time in milliseconds, defaults to 30 seconds, pass `0` to disable the timeout.
            The default value can be changed by using the browserContext.set_default_timeout(timeout) or
            page.set_default_timeout(timeout) methods.
        """
        event = "console"
        return EventContextManager(
            self, self._impl_obj.wait_for_event(event, predicate, timeout)
        )

    def expect_download(
        self,
        predicate: typing.Union[typing.Callable[["Download"], bool]] = None,
        timeout: float = None,
    ) -> EventContextManager["Download"]:
        """Page.expect_download

        Returns context manager that waits for ``event`` to fire upon exit. It passes event's value
        into the ``predicate`` function and waits for the predicate to return a truthy value. Will throw
        an error if the page is closed before the ``event`` is fired.

        with page.expect_download() as event_info:
            page.click("button")
        value = event_info.value

        Parameters
        ----------
        predicate : Optional[typing.Callable[[Any], bool]]
            Predicate receiving event data.
        timeout : Optional[int]
            Maximum wait time in milliseconds, defaults to 30 seconds, pass `0` to disable the timeout.
            The default value can be changed by using the browserContext.set_default_timeout(timeout) or
            page.set_default_timeout(timeout) methods.
        """
        event = "download"
        return EventContextManager(
            self, self._impl_obj.wait_for_event(event, predicate, timeout)
        )

    def expect_file_chooser(
        self,
        predicate: typing.Union[typing.Callable[["FileChooser"], bool]] = None,
        timeout: float = None,
    ) -> EventContextManager["FileChooser"]:
        """Page.expect_file_chooser

        Returns context manager that waits for ``event`` to fire upon exit. It passes event's value
        into the ``predicate`` function and waits for the predicate to return a truthy value. Will throw
        an error if the page is closed before the ``event`` is fired.

        with page.expect_filechooser() as event_info:
            page.click("button")
        value = event_info.value

        Parameters
        ----------
        predicate : Optional[typing.Callable[[Any], bool]]
            Predicate receiving event data.
        timeout : Optional[int]
            Maximum wait time in milliseconds, defaults to 30 seconds, pass `0` to disable the timeout.
            The default value can be changed by using the browserContext.set_default_timeout(timeout) or
            page.set_default_timeout(timeout) methods.
        """
        event = "filechooser"
        return EventContextManager(
            self, self._impl_obj.wait_for_event(event, predicate, timeout)
        )

    def expect_load_state(
        self,
        state: Literal["domcontentloaded", "load", "networkidle"] = None,
        timeout: float = None,
    ) -> EventContextManager[typing.Union["Response", NoneType]]:
        """Page.expect_load_state

        Returns context manager that waits for ``event`` to fire upon exit. It passes event's value
        into the ``predicate`` function and waits for the predicate to return a truthy value. Will throw
        an error if the page is closed before the ``event`` is fired.

        with page.expect_loadstate() as event_info:
            page.click("button")
        value = event_info.value

        Parameters
        ----------
        predicate : Optional[typing.Callable[[Any], bool]]
            Predicate receiving event data.
        timeout : Optional[int]
            Maximum wait time in milliseconds, defaults to 30 seconds, pass `0` to disable the timeout.
            The default value can be changed by using the browserContext.set_default_timeout(timeout) or
            page.set_default_timeout(timeout) methods.
        """
        return EventContextManager(
            self, self._impl_obj.wait_for_load_state(state, timeout)
        )

    def expect_navigation(
        self,
        url: typing.Union[str, typing.Pattern, typing.Callable[[str], bool]] = None,
        wait_until: Literal["domcontentloaded", "load", "networkidle"] = None,
        timeout: float = None,
    ) -> EventContextManager[typing.Union["Response", NoneType]]:
        """Page.expect_navigation

        Returns context manager that waits for ``event`` to fire upon exit. It passes event's value
        into the ``predicate`` function and waits for the predicate to return a truthy value. Will throw
        an error if the page is closed before the ``event`` is fired.

        with page.expect_navigation() as event_info:
            page.click("button")
        value = event_info.value

        Parameters
        ----------
        predicate : Optional[typing.Callable[[Any], bool]]
            Predicate receiving event data.
        timeout : Optional[int]
            Maximum wait time in milliseconds, defaults to 30 seconds, pass `0` to disable the timeout.
            The default value can be changed by using the browserContext.set_default_timeout(timeout) or
            page.set_default_timeout(timeout) methods.
        """
        return EventContextManager(
            self, self._impl_obj.wait_for_navigation(url, wait_until, timeout)
        )

    def expect_popup(
        self,
        predicate: typing.Union[typing.Callable[["Page"], bool]] = None,
        timeout: float = None,
    ) -> EventContextManager["Page"]:
        """Page.expect_popup

        Returns context manager that waits for ``event`` to fire upon exit. It passes event's value
        into the ``predicate`` function and waits for the predicate to return a truthy value. Will throw
        an error if the page is closed before the ``event`` is fired.

        with page.expect_popup() as event_info:
            page.click("button")
        value = event_info.value

        Parameters
        ----------
        predicate : Optional[typing.Callable[[Any], bool]]
            Predicate receiving event data.
        timeout : Optional[int]
            Maximum wait time in milliseconds, defaults to 30 seconds, pass `0` to disable the timeout.
            The default value can be changed by using the browserContext.set_default_timeout(timeout) or
            page.set_default_timeout(timeout) methods.
        """
        event = "popup"
        return EventContextManager(
            self, self._impl_obj.wait_for_event(event, predicate, timeout)
        )

    def expect_request(
        self,
        url_or_predicate: typing.Union[
            str, typing.Pattern, typing.Callable[["Request"], bool]
        ],
        timeout: float = None,
    ) -> EventContextManager["Request"]:
        """Page.expect_request

        Returns context manager that waits for ``event`` to fire upon exit. It passes event's value
        into the ``predicate`` function and waits for the predicate to return a truthy value. Will throw
        an error if the page is closed before the ``event`` is fired.

        with page.expect_request() as event_info:
            page.click("button")
        value = event_info.value

        Parameters
        ----------
        predicate : Optional[typing.Callable[[Any], bool]]
            Predicate receiving event data.
        timeout : Optional[int]
            Maximum wait time in milliseconds, defaults to 30 seconds, pass `0` to disable the timeout.
            The default value can be changed by using the browserContext.set_default_timeout(timeout) or
            page.set_default_timeout(timeout) methods.
        """
        return EventContextManager(
            self, self._impl_obj.wait_for_request(url_or_predicate, timeout)
        )

    def expect_response(
        self,
        url_or_predicate: typing.Union[
            str, typing.Pattern, typing.Callable[["Response"], bool]
        ],
        timeout: float = None,
    ) -> EventContextManager["Response"]:
        """Page.expect_response

        Returns context manager that waits for ``event`` to fire upon exit. It passes event's value
        into the ``predicate`` function and waits for the predicate to return a truthy value. Will throw
        an error if the page is closed before the ``event`` is fired.

        with page.expect_response() as event_info:
            page.click("button")
        value = event_info.value

        Parameters
        ----------
        predicate : Optional[typing.Callable[[Any], bool]]
            Predicate receiving event data.
        timeout : Optional[int]
            Maximum wait time in milliseconds, defaults to 30 seconds, pass `0` to disable the timeout.
            The default value can be changed by using the browserContext.set_default_timeout(timeout) or
            page.set_default_timeout(timeout) methods.
        """
        return EventContextManager(
            self, self._impl_obj.wait_for_response(url_or_predicate, timeout)
        )

    def expect_worker(
        self,
        predicate: typing.Union[typing.Callable[["Worker"], bool]] = None,
        timeout: float = None,
    ) -> EventContextManager["Worker"]:
        """Page.expect_worker

        Returns context manager that waits for ``event`` to fire upon exit. It passes event's value
        into the ``predicate`` function and waits for the predicate to return a truthy value. Will throw
        an error if the page is closed before the ``event`` is fired.

        with page.expect_worker() as event_info:
            page.click("button")
        value = event_info.value

        Parameters
        ----------
        predicate : Optional[typing.Callable[[Any], bool]]
            Predicate receiving event data.
        timeout : Optional[int]
            Maximum wait time in milliseconds, defaults to 30 seconds, pass `0` to disable the timeout.
            The default value can be changed by using the browserContext.set_default_timeout(timeout) or
            page.set_default_timeout(timeout) methods.
        """
        event = "worker"
        return EventContextManager(
            self, self._impl_obj.wait_for_event(event, predicate, timeout)
        )


mapping.register(PageImpl, Page)


class BrowserContext(SyncBase):
    def __init__(self, obj: BrowserContextImpl):
        super().__init__(obj)

    @property
    def pages(self) -> typing.List["Page"]:
        """BrowserContext.pages

        Returns all open pages in the context. Non visible pages, such as `"background_page"`, will not be listed here. You can
        find them using `chromium_browser_context.background_pages()`.

        Returns
        -------
        List[Page]
        """
        return mapping.from_impl_list(self._impl_obj.pages)

    @property
    def browser(self) -> typing.Union["Browser", NoneType]:
        """BrowserContext.browser

        Returns the browser instance of the context. If it was launched as a persistent context null gets returned.

        Returns
        -------
        Union[Browser, NoneType]
        """
        return mapping.from_impl_nullable(self._impl_obj.browser)

    def set_default_navigation_timeout(self, timeout: float) -> NoneType:
        """BrowserContext.set_default_navigation_timeout

        This setting will change the default maximum navigation time for the following methods and related shortcuts:
        - `page.go_back()`
        - `page.go_forward()`
        - `page.goto()`
        - `page.reload()`
        - `page.set_content()`
        - `page.wait_for_navigation()`

        > **NOTE** `page.set_default_navigation_timeout()` and `page.set_default_timeout()` take priority over
        `browser_context.set_default_navigation_timeout()`.

        Parameters
        ----------
        timeout : float
            Maximum navigation time in milliseconds
        """

        try:
            log_api("=> browser_context.set_default_navigation_timeout started")
            result = mapping.from_maybe_impl(
                self._impl_obj.set_default_navigation_timeout(timeout=timeout)
            )
            log_api("<= browser_context.set_default_navigation_timeout succeded")
            return result
        except Exception as e:
            log_api("<= browser_context.set_default_navigation_timeout failed")
            raise e

    def set_default_timeout(self, timeout: float) -> NoneType:
        """BrowserContext.set_default_timeout

        This setting will change the default maximum time for all the methods accepting `timeout` option.

        > **NOTE** `page.set_default_navigation_timeout()`, `page.set_default_timeout()` and
        `browser_context.set_default_navigation_timeout()` take priority over `browser_context.set_default_timeout()`.

        Parameters
        ----------
        timeout : float
            Maximum time in milliseconds
        """

        try:
            log_api("=> browser_context.set_default_timeout started")
            result = mapping.from_maybe_impl(
                self._impl_obj.set_default_timeout(timeout=timeout)
            )
            log_api("<= browser_context.set_default_timeout succeded")
            return result
        except Exception as e:
            log_api("<= browser_context.set_default_timeout failed")
            raise e

    def new_page(self) -> "Page":
        """BrowserContext.new_page

        Creates a new page in the browser context.

        Returns
        -------
        Page
        """

        try:
            log_api("=> browser_context.new_page started")
            result = mapping.from_impl(self._sync(self._impl_obj.new_page()))
            log_api("<= browser_context.new_page succeded")
            return result
        except Exception as e:
            log_api("<= browser_context.new_page failed")
            raise e

    def cookies(
        self, urls: typing.Union[str, typing.List[str]] = None
    ) -> typing.List["Cookie"]:
        """BrowserContext.cookies

        If no URLs are specified, this method returns all cookies. If URLs are specified, only cookies that affect those URLs
        are returned.

        Parameters
        ----------
        urls : Union[List[str], str, NoneType]
            Optional list of URLs.

        Returns
        -------
        List[{name: str, value: str, url: Union[str, NoneType], domain: Union[str, NoneType], path: Union[str, NoneType], expires: Union[float, NoneType], httpOnly: Union[bool, NoneType], secure: Union[bool, NoneType], sameSite: Union["Strict", "Lax", "None", NoneType]}]
        """

        try:
            log_api("=> browser_context.cookies started")
            result = mapping.from_impl_list(
                self._sync(self._impl_obj.cookies(urls=urls))
            )
            log_api("<= browser_context.cookies succeded")
            return result
        except Exception as e:
            log_api("<= browser_context.cookies failed")
            raise e

    def add_cookies(self, cookies: typing.List["Cookie"]) -> NoneType:
        """BrowserContext.add_cookies

        Adds cookies into this browser context. All pages within this context will have these cookies installed. Cookies can be
        obtained via `browser_context.cookies()`.

        Parameters
        ----------
        cookies : List[{name: str, value: str, url: Union[str, NoneType], domain: Union[str, NoneType], path: Union[str, NoneType], expires: Union[float, NoneType], httpOnly: Union[bool, NoneType], secure: Union[bool, NoneType], sameSite: Union["Strict", "Lax", "None", NoneType]}]
        """

        try:
            log_api("=> browser_context.add_cookies started")
            result = mapping.from_maybe_impl(
                self._sync(self._impl_obj.add_cookies(cookies=cookies))
            )
            log_api("<= browser_context.add_cookies succeded")
            return result
        except Exception as e:
            log_api("<= browser_context.add_cookies failed")
            raise e

    def clear_cookies(self) -> NoneType:
        """BrowserContext.clear_cookies

        Clears context cookies.
        """

        try:
            log_api("=> browser_context.clear_cookies started")
            result = mapping.from_maybe_impl(self._sync(self._impl_obj.clear_cookies()))
            log_api("<= browser_context.clear_cookies succeded")
            return result
        except Exception as e:
            log_api("<= browser_context.clear_cookies failed")
            raise e

    def grant_permissions(
        self, permissions: typing.List[str], origin: str = None
    ) -> NoneType:
        """BrowserContext.grant_permissions

        Grants specified permissions to the browser context. Only grants corresponding permissions to the given origin if
        specified.

        Parameters
        ----------
        permissions : List[str]
            A permission or an array of permissions to grant. Permissions can be one of the following values:
            - `'geolocation'`
            - `'midi'`
            - `'midi-sysex'` (system-exclusive midi)
            - `'notifications'`
            - `'push'`
            - `'camera'`
            - `'microphone'`
            - `'background-sync'`
            - `'ambient-light-sensor'`
            - `'accelerometer'`
            - `'gyroscope'`
            - `'magnetometer'`
            - `'accessibility-events'`
            - `'clipboard-read'`
            - `'clipboard-write'`
            - `'payment-handler'`
        origin : Union[str, NoneType]
            The [origin] to grant permissions to, e.g. "https://example.com".
        """

        try:
            log_api("=> browser_context.grant_permissions started")
            result = mapping.from_maybe_impl(
                self._sync(
                    self._impl_obj.grant_permissions(
                        permissions=permissions, origin=origin
                    )
                )
            )
            log_api("<= browser_context.grant_permissions succeded")
            return result
        except Exception as e:
            log_api("<= browser_context.grant_permissions failed")
            raise e

    def clear_permissions(self) -> NoneType:
        """BrowserContext.clear_permissions

        Clears all permission overrides for the browser context.
        """

        try:
            log_api("=> browser_context.clear_permissions started")
            result = mapping.from_maybe_impl(
                self._sync(self._impl_obj.clear_permissions())
            )
            log_api("<= browser_context.clear_permissions succeded")
            return result
        except Exception as e:
            log_api("<= browser_context.clear_permissions failed")
            raise e

    def set_geolocation(
        self, latitude: float, longitude: float, accuracy: float = None
    ) -> NoneType:
        """BrowserContext.set_geolocation

        Sets the context's geolocation. Passing `null` or `undefined` emulates position unavailable.

        > **NOTE** Consider using `browser_context.grant_permissions()` to grant permissions for the browser context pages
        to read its geolocation.

        Parameters
        ----------
        latitude : float
            Latitude between -90 and 90. **required**
        longitude : float
            Longitude between -180 and 180. **required**
        accuracy : Union[float, NoneType]
            Non-negative accuracy value. Defaults to `0`.
        """

        try:
            log_api("=> browser_context.set_geolocation started")
            result = mapping.from_maybe_impl(
                self._sync(
                    self._impl_obj.set_geolocation(
                        latitude=latitude, longitude=longitude, accuracy=accuracy
                    )
                )
            )
            log_api("<= browser_context.set_geolocation succeded")
            return result
        except Exception as e:
            log_api("<= browser_context.set_geolocation failed")
            raise e

    def reset_geolocation(self) -> NoneType:

        try:
            log_api("=> browser_context.reset_geolocation started")
            result = mapping.from_maybe_impl(
                self._sync(self._impl_obj.reset_geolocation())
            )
            log_api("<= browser_context.reset_geolocation succeded")
            return result
        except Exception as e:
            log_api("<= browser_context.reset_geolocation failed")
            raise e

    def set_extra_http_headers(self, headers: typing.Dict[str, str]) -> NoneType:
        """BrowserContext.set_extra_http_headers

        The extra HTTP headers will be sent with every request initiated by any page in the context. These headers are merged
        with page-specific extra HTTP headers set with `page.set_extra_http_headers()`. If page overrides a particular
        header, page-specific header value will be used instead of the browser context header value.

        > **NOTE** `browserContext.setExtraHTTPHeaders` does not guarantee the order of headers in the outgoing requests.

        Parameters
        ----------
        headers : Dict[str, str]
            An object containing additional HTTP headers to be sent with every request. All header values must be strings.
        """

        try:
            log_api("=> browser_context.set_extra_http_headers started")
            result = mapping.from_maybe_impl(
                self._sync(
                    self._impl_obj.set_extra_http_headers(
                        headers=mapping.to_impl(headers)
                    )
                )
            )
            log_api("<= browser_context.set_extra_http_headers succeded")
            return result
        except Exception as e:
            log_api("<= browser_context.set_extra_http_headers failed")
            raise e

    def set_offline(self, offline: bool) -> NoneType:
        """BrowserContext.set_offline

        Parameters
        ----------
        offline : bool
            Whether to emulate network being offline for the browser context.
        """

        try:
            log_api("=> browser_context.set_offline started")
            result = mapping.from_maybe_impl(
                self._sync(self._impl_obj.set_offline(offline=offline))
            )
            log_api("<= browser_context.set_offline succeded")
            return result
        except Exception as e:
            log_api("<= browser_context.set_offline failed")
            raise e

    def add_init_script(
        self, script: str = None, path: typing.Union[str, pathlib.Path] = None
    ) -> NoneType:
        """BrowserContext.add_init_script

        Adds a script which would be evaluated in one of the following scenarios:
        - Whenever a page is created in the browser context or is navigated.
        - Whenever a child frame is attached or navigated in any page in the browser context. In this case, the script is
          evaluated in the context of the newly attached frame.

        The script is evaluated after the document was created but before any of its scripts were run. This is useful to amend
        the JavaScript environment, e.g. to seed `Math.random`.

        An example of overriding `Math.random` before the page loads:

        > **NOTE** The order of evaluation of multiple scripts installed via `browser_context.add_init_script()` and
        `page.add_init_script()` is not defined.

        Parameters
        ----------
        script : Union[str, NoneType]
            Script to be evaluated in all pages in the browser context.
        """

        try:
            log_api("=> browser_context.add_init_script started")
            result = mapping.from_maybe_impl(
                self._sync(self._impl_obj.add_init_script(script=script, path=path))
            )
            log_api("<= browser_context.add_init_script succeded")
            return result
        except Exception as e:
            log_api("<= browser_context.add_init_script failed")
            raise e

    def expose_binding(
        self, name: str, callback: typing.Callable, handle: bool = None
    ) -> NoneType:
        """BrowserContext.expose_binding

        The method adds a function called `name` on the `window` object of every frame in every page in the context. When
        called, the function executes `callback` and returns a [Promise] which resolves to the return value of `callback`. If
        the `callback` returns a [Promise], it will be awaited.

        The first argument of the `callback` function contains information about the caller: `{ browserContext: BrowserContext,
        page: Page, frame: Frame }`.

        See `page.expose_binding()` for page-only version.

        An example of exposing page URL to all frames in all pages in the context:

        An example of passing an element handle:

        Parameters
        ----------
        name : str
            Name of the function on the window object.
        callback : Callable
            Callback function that will be called in the Playwright's context.
        handle : Union[bool, NoneType]
            Whether to pass the argument as a handle, instead of passing by value. When passing a handle, only one argument is
            supported. When passing by value, multiple arguments are supported.
        """

        try:
            log_api("=> browser_context.expose_binding started")
            result = mapping.from_maybe_impl(
                self._sync(
                    self._impl_obj.expose_binding(
                        name=name, callback=self._wrap_handler(callback), handle=handle
                    )
                )
            )
            log_api("<= browser_context.expose_binding succeded")
            return result
        except Exception as e:
            log_api("<= browser_context.expose_binding failed")
            raise e

    def expose_function(self, name: str, callback: typing.Callable) -> NoneType:
        """BrowserContext.expose_function

        The method adds a function called `name` on the `window` object of every frame in every page in the context. When
        called, the function executes `callback` and returns a [Promise] which resolves to the return value of `callback`.

        If the `callback` returns a [Promise], it will be awaited.

        See `page.expose_function()` for page-only version.

        An example of adding an `md5` function to all pages in the context:

        Parameters
        ----------
        name : str
            Name of the function on the window object.
        callback : Callable
            Callback function that will be called in the Playwright's context.
        """

        try:
            log_api("=> browser_context.expose_function started")
            result = mapping.from_maybe_impl(
                self._sync(
                    self._impl_obj.expose_function(
                        name=name, callback=self._wrap_handler(callback)
                    )
                )
            )
            log_api("<= browser_context.expose_function succeded")
            return result
        except Exception as e:
            log_api("<= browser_context.expose_function failed")
            raise e

    def route(
        self,
        url: typing.Union[str, typing.Pattern, typing.Callable[[str], bool]],
        handler: typing.Union[
            typing.Callable[["Route"], typing.Any],
            typing.Callable[["Route", "Request"], typing.Any],
        ],
    ) -> NoneType:
        """BrowserContext.route

        Routing provides the capability to modify network requests that are made by any page in the browser context. Once route
        is enabled, every request matching the url pattern will stall unless it's continued, fulfilled or aborted.

        An example of a naïve handler that aborts all image requests:

        or the same snippet using a regex pattern instead:

        Page routes (set up with `page.route()`) take precedence over browser context routes when request matches both
        handlers.

        > **NOTE** Enabling routing disables http cache.

        Parameters
        ----------
        url : Union[Callable[[str], bool], Pattern, str]
            A glob pattern, regex pattern or predicate receiving [URL] to match while routing.
        handler : Union[Callable[[Route, Request], Any], Callable[[Route], Any]]
            handler function to route the request.
        """

        try:
            log_api("=> browser_context.route started")
            result = mapping.from_maybe_impl(
                self._sync(
                    self._impl_obj.route(
                        url=self._wrap_handler(url), handler=self._wrap_handler(handler)
                    )
                )
            )
            log_api("<= browser_context.route succeded")
            return result
        except Exception as e:
            log_api("<= browser_context.route failed")
            raise e

    def unroute(
        self,
        url: typing.Union[str, typing.Pattern, typing.Callable[[str], bool]],
        handler: typing.Union[
            typing.Callable[["Route"], typing.Any],
            typing.Callable[["Route", "Request"], typing.Any],
        ] = None,
    ) -> NoneType:
        """BrowserContext.unroute

        Removes a route created with `browser_context.route()`. When `handler` is not specified, removes all routes for
        the `url`.

        Parameters
        ----------
        url : Union[Callable[[str], bool], Pattern, str]
            A glob pattern, regex pattern or predicate receiving [URL] used to register a routing with
            `browser_context.route()`.
        handler : Union[Callable[[Route, Request], Any], Callable[[Route], Any], NoneType]
            Optional handler function used to register a routing with `browser_context.route()`.
        """

        try:
            log_api("=> browser_context.unroute started")
            result = mapping.from_maybe_impl(
                self._sync(
                    self._impl_obj.unroute(
                        url=self._wrap_handler(url), handler=self._wrap_handler(handler)
                    )
                )
            )
            log_api("<= browser_context.unroute succeded")
            return result
        except Exception as e:
            log_api("<= browser_context.unroute failed")
            raise e

    def wait_for_event(
        self,
        event: str,
        predicate: typing.Union[typing.Callable[[typing.Any], bool]] = None,
        timeout: float = None,
    ) -> typing.Any:
        """BrowserContext.wait_for_event

        Waits for event to fire and passes its value into the predicate function. Returns when the predicate returns truthy
        value. Will throw an error if the context closes before the event is fired. Returns the event data value.

        Parameters
        ----------
        event : str
            Event name, same one would pass into `browserContext.on(event)`.
        predicate : Union[Callable[[Any], bool], NoneType]
            receives the event data and resolves to truthy value when the waiting should resolve.
        timeout : Union[float, NoneType]
            maximum time to wait for in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default
            value can be changed by using the `browser_context.set_default_timeout()`.

        Returns
        -------
        Any
        """

        try:
            log_api("=> browser_context.wait_for_event started")
            result = mapping.from_maybe_impl(
                self._sync(
                    self._impl_obj.wait_for_event(
                        event=event,
                        predicate=self._wrap_handler(predicate),
                        timeout=timeout,
                    )
                )
            )
            log_api("<= browser_context.wait_for_event succeded")
            return result
        except Exception as e:
            log_api("<= browser_context.wait_for_event failed")
            raise e

    def close(self) -> NoneType:
        """BrowserContext.close

        Closes the browser context. All the pages that belong to the browser context will be closed.

        > **NOTE** the default browser context cannot be closed.
        """

        try:
            log_api("=> browser_context.close started")
            result = mapping.from_maybe_impl(self._sync(self._impl_obj.close()))
            log_api("<= browser_context.close succeded")
            return result
        except Exception as e:
            log_api("<= browser_context.close failed")
            raise e

    def storage_state(
        self, path: typing.Union[str, pathlib.Path] = None
    ) -> "StorageState":
        """BrowserContext.storage_state

        Returns storage state for this browser context, contains current cookies and local storage snapshot.

        Parameters
        ----------
        path : Union[pathlib.Path, str, NoneType]
            The file path to save the storage state to. If `path` is a relative path, then it is resolved relative to
            [current working directory](https://nodejs.org/api/process.html#process_process_cwd). If no path is provided, storage
            state is still returned, but won't be saved to the disk.

        Returns
        -------
        {cookies: Union[List[{name: str, value: str, url: Union[str, NoneType], domain: Union[str, NoneType], path: Union[str, NoneType], expires: Union[float, NoneType], httpOnly: Union[bool, NoneType], secure: Union[bool, NoneType], sameSite: Union["Strict", "Lax", "None", NoneType]}], NoneType], origins: Union[List[Dict], NoneType]}
        """

        try:
            log_api("=> browser_context.storage_state started")
            result = mapping.from_impl(
                self._sync(self._impl_obj.storage_state(path=path))
            )
            log_api("<= browser_context.storage_state succeded")
            return result
        except Exception as e:
            log_api("<= browser_context.storage_state failed")
            raise e

    def expect_event(
        self,
        event: str,
        predicate: typing.Union[typing.Callable[[typing.Any], bool]] = None,
        timeout: float = None,
    ) -> EventContextManager:
        """BrowserContext.expect_event

        Returns context manager that waits for ``event`` to fire upon exit. It passes event's value
        into the ``predicate`` function and waits for the predicate to return a truthy value. Will throw
        an error if the page is closed before the ``event`` is fired.

        with page.expect_event() as event_info:
            page.click("button")
        value = event_info.value

        Parameters
        ----------
        predicate : Optional[typing.Callable[[Any], bool]]
            Predicate receiving event data.
        timeout : Optional[int]
            Maximum wait time in milliseconds, defaults to 30 seconds, pass `0` to disable the timeout.
            The default value can be changed by using the browserContext.set_default_timeout(timeout) or
            page.set_default_timeout(timeout) methods.
        """
        return EventContextManager(
            self, self._impl_obj.wait_for_event(event, predicate, timeout)
        )

    def expect_page(
        self,
        predicate: typing.Union[typing.Callable[["Page"], bool]] = None,
        timeout: float = None,
    ) -> EventContextManager["Page"]:
        """BrowserContext.expect_page

        Returns context manager that waits for ``event`` to fire upon exit. It passes event's value
        into the ``predicate`` function and waits for the predicate to return a truthy value. Will throw
        an error if the page is closed before the ``event`` is fired.

        with page.expect_page() as event_info:
            page.click("button")
        value = event_info.value

        Parameters
        ----------
        predicate : Optional[typing.Callable[[Any], bool]]
            Predicate receiving event data.
        timeout : Optional[int]
            Maximum wait time in milliseconds, defaults to 30 seconds, pass `0` to disable the timeout.
            The default value can be changed by using the browserContext.set_default_timeout(timeout) or
            page.set_default_timeout(timeout) methods.
        """
        event = "page"
        return EventContextManager(
            self, self._impl_obj.wait_for_event(event, predicate, timeout)
        )


mapping.register(BrowserContextImpl, BrowserContext)


class CDPSession(SyncBase):
    def __init__(self, obj: CDPSessionImpl):
        super().__init__(obj)

    def send(self, method: str, params: typing.Dict = None) -> typing.Dict:
        """CDPSession.send

        Parameters
        ----------
        method : str
            protocol method name
        params : Union[Dict, NoneType]
            Optional method parameters

        Returns
        -------
        Dict
        """

        try:
            log_api("=> cdp_session.send started")
            result = mapping.from_maybe_impl(
                self._sync(
                    self._impl_obj.send(method=method, params=mapping.to_impl(params))
                )
            )
            log_api("<= cdp_session.send succeded")
            return result
        except Exception as e:
            log_api("<= cdp_session.send failed")
            raise e

    def detach(self) -> NoneType:
        """CDPSession.detach

        Detaches the CDPSession from the target. Once detached, the CDPSession object won't emit any events and can't be used to
        send messages.
        """

        try:
            log_api("=> cdp_session.detach started")
            result = mapping.from_maybe_impl(self._sync(self._impl_obj.detach()))
            log_api("<= cdp_session.detach succeded")
            return result
        except Exception as e:
            log_api("<= cdp_session.detach failed")
            raise e


mapping.register(CDPSessionImpl, CDPSession)


class ChromiumBrowserContext(BrowserContext):
    def __init__(self, obj: ChromiumBrowserContextImpl):
        super().__init__(obj)

    def background_pages(self) -> typing.List["Page"]:
        """ChromiumBrowserContext.background_pages

        All existing background pages in the context.

        Returns
        -------
        List[Page]
        """

        try:
            log_api("=> chromium_browser_context.background_pages started")
            result = mapping.from_impl_list(self._impl_obj.background_pages())
            log_api("<= chromium_browser_context.background_pages succeded")
            return result
        except Exception as e:
            log_api("<= chromium_browser_context.background_pages failed")
            raise e

    def service_workers(self) -> typing.List["Worker"]:
        """ChromiumBrowserContext.service_workers

        All existing service workers in the context.

        Returns
        -------
        List[Worker]
        """

        try:
            log_api("=> chromium_browser_context.service_workers started")
            result = mapping.from_impl_list(self._impl_obj.service_workers())
            log_api("<= chromium_browser_context.service_workers succeded")
            return result
        except Exception as e:
            log_api("<= chromium_browser_context.service_workers failed")
            raise e

    def new_cdp_session(self, page: "Page") -> "CDPSession":
        """ChromiumBrowserContext.new_cdp_session

        Returns the newly created session.

        Parameters
        ----------
        page : Page
            Page to create new session for.

        Returns
        -------
        CDPSession
        """

        try:
            log_api("=> chromium_browser_context.new_cdp_session started")
            result = mapping.from_impl(
                self._sync(self._impl_obj.new_cdp_session(page=page._impl_obj))
            )
            log_api("<= chromium_browser_context.new_cdp_session succeded")
            return result
        except Exception as e:
            log_api("<= chromium_browser_context.new_cdp_session failed")
            raise e


mapping.register(ChromiumBrowserContextImpl, ChromiumBrowserContext)


class Browser(SyncBase):
    def __init__(self, obj: BrowserImpl):
        super().__init__(obj)

    @property
    def contexts(self) -> typing.List["BrowserContext"]:
        """Browser.contexts

        Returns an array of all open browser contexts. In a newly created browser, this will return zero browser contexts.

        Returns
        -------
        List[BrowserContext]
        """
        return mapping.from_impl_list(self._impl_obj.contexts)

    @property
    def version(self) -> str:
        """Browser.version

        Returns the browser version.

        Returns
        -------
        str
        """
        return mapping.from_maybe_impl(self._impl_obj.version)

    def is_connected(self) -> bool:
        """Browser.is_connected

        Indicates that the browser is connected.

        Returns
        -------
        bool
        """

        try:
            log_api("=> browser.is_connected started")
            result = mapping.from_maybe_impl(self._impl_obj.is_connected())
            log_api("<= browser.is_connected succeded")
            return result
        except Exception as e:
            log_api("<= browser.is_connected failed")
            raise e

    def new_context(
        self,
        viewport: typing.Union[typing.Tuple[int, int], Literal[0]] = None,
        ignore_https_errors: bool = None,
        java_script_enabled: bool = None,
        bypass_csp: bool = None,
        user_agent: str = None,
        locale: str = None,
        timezone_id: str = None,
        geolocation: "Geolocation" = None,
        permissions: typing.List[str] = None,
        extra_http_headers: typing.Union[typing.Dict[str, str]] = None,
        offline: bool = None,
        http_credentials: typing.Union[typing.Tuple[str, str]] = None,
        device_scale_factor: float = None,
        is_mobile: bool = None,
        has_touch: bool = None,
        color_scheme: Literal["dark", "light", "no-preference"] = None,
        accept_downloads: bool = None,
        default_browser_type: str = None,
        proxy: "ProxySettings" = None,
        record_har_path: typing.Union[str, pathlib.Path] = None,
        record_har_omit_content: bool = None,
        record_video_dir: typing.Union[str, pathlib.Path] = None,
        record_video_size: typing.Union[typing.Tuple[int, int]] = None,
        storage_state: typing.Union["StorageState", str, pathlib.Path] = None,
    ) -> "BrowserContext":
        """Browser.new_context

        Creates a new browser context. It won't share cookies/cache with other browser contexts.

        Parameters
        ----------
        viewport : Union["0", typing.Tuple[int, int], NoneType]
            Sets a consistent viewport for each page. Defaults to an 1280x720 viewport. `null` disables the default viewport.
        ignore_https_errors : Union[bool, NoneType]
            Whether to ignore HTTPS errors during navigation. Defaults to `false`.
        java_script_enabled : Union[bool, NoneType]
            Whether or not to enable JavaScript in the context. Defaults to `true`.
        bypass_csp : Union[bool, NoneType]
            Toggles bypassing page's Content-Security-Policy.
        user_agent : Union[str, NoneType]
            Specific user agent to use in this context.
        locale : Union[str, NoneType]
            Specify user locale, for example `en-GB`, `de-DE`, etc. Locale will affect `navigator.language` value, `Accept-Language`
            request header value as well as number and date formatting rules.
        timezone_id : Union[str, NoneType]
            Changes the timezone of the context. See
            [ICU's metaZones.txt](https://cs.chromium.org/chromium/src/third_party/icu/source/data/misc/metaZones.txt?rcl=faee8bc70570192d82d2978a71e2a615788597d1)
            for a list of supported timezone IDs.
        geolocation : Union[{latitude: float, longitude: float, accuracy: Union[float, NoneType]}, NoneType]
        permissions : Union[List[str], NoneType]
            A list of permissions to grant to all pages in this context. See `browser_context.grant_permissions()` for more
            details.
        extra_http_headers : Union[Dict[str, str], NoneType]
            An object containing additional HTTP headers to be sent with every request. All header values must be strings.
        offline : Union[bool, NoneType]
            Whether to emulate network being offline. Defaults to `false`.
        http_credentials : Union[typing.Tuple[str, str], NoneType]
            Credentials for [HTTP authentication](https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication).
        device_scale_factor : Union[float, NoneType]
            Specify device scale factor (can be thought of as dpr). Defaults to `1`.
        is_mobile : Union[bool, NoneType]
            Whether the `meta viewport` tag is taken into account and touch events are enabled. Defaults to `false`. Not supported
            in Firefox.
        has_touch : Union[bool, NoneType]
            Specifies if viewport supports touch events. Defaults to false.
        color_scheme : Union["dark", "light", "no-preference", NoneType]
            Emulates `'prefers-colors-scheme'` media feature, supported values are `'light'`, `'dark'`, `'no-preference'`. See
            `page.emulate_media()` for more details. Defaults to '`light`'.
        accept_downloads : Union[bool, NoneType]
            Whether to automatically download all the attachments. Defaults to `false` where all the downloads are canceled.
        proxy : Union[{server: str, bypass: Union[str, NoneType], username: Union[str, NoneType], password: Union[str, NoneType]}, NoneType]
            Network proxy settings to use with this context. Note that browser needs to be launched with the global proxy for this
            option to work. If all contexts override the proxy, global proxy will be never used and can be any string, for example
            `launch({ proxy: { server: 'per-context' } })`.
        record_har_path : Union[pathlib.Path, str, NoneType]
            Path on the filesystem to write the HAR file to.
        record_har_omit_content : Union[bool, NoneType]
            Optional setting to control whether to omit request content from the HAR. Defaults to `false`.
        record_video_dir : Union[pathlib.Path, str, NoneType]
            Path to the directory to put videos into.
        record_video_size : Union[typing.Tuple[int, int], NoneType]
            Optional dimensions of the recorded videos. If not specified the size will be equal to `viewport`. If `viewport` is not
            configured explicitly the video size defaults to 1280x720. Actual picture of each page will be scaled down if necessary
            to fit the specified size.
        storage_state : Union[pathlib.Path, str, {cookies: Union[List[{name: str, value: str, url: Union[str, NoneType], domain: Union[str, NoneType], path: Union[str, NoneType], expires: Union[float, NoneType], httpOnly: Union[bool, NoneType], secure: Union[bool, NoneType], sameSite: Union["Strict", "Lax", "None", NoneType]}], NoneType], origins: Union[List[Dict], NoneType]}, NoneType]
            Populates context with given storage state. This method can be used to initialize context with logged-in information
            obtained via `browser_context.storage_state()`. Either a path to the file with saved storage, or an object with
            the following fields:

        Returns
        -------
        BrowserContext
        """

        try:
            log_api("=> browser.new_context started")
            result = mapping.from_impl(
                self._sync(
                    self._impl_obj.new_context(
                        viewport=viewport,
                        ignoreHTTPSErrors=ignore_https_errors,
                        javaScriptEnabled=java_script_enabled,
                        bypassCSP=bypass_csp,
                        userAgent=user_agent,
                        locale=locale,
                        timezoneId=timezone_id,
                        geolocation=geolocation,
                        permissions=permissions,
                        extraHTTPHeaders=mapping.to_impl(extra_http_headers),
                        offline=offline,
                        httpCredentials=http_credentials,
                        deviceScaleFactor=device_scale_factor,
                        isMobile=is_mobile,
                        hasTouch=has_touch,
                        colorScheme=color_scheme,
                        acceptDownloads=accept_downloads,
                        defaultBrowserType=default_browser_type,
                        proxy=proxy,
                        recordHarPath=record_har_path,
                        recordHarOmitContent=record_har_omit_content,
                        recordVideoDir=record_video_dir,
                        recordVideoSize=record_video_size,
                        storageState=storage_state,
                    )
                )
            )
            log_api("<= browser.new_context succeded")
            return result
        except Exception as e:
            log_api("<= browser.new_context failed")
            raise e

    def new_page(
        self,
        viewport: typing.Union[typing.Tuple[int, int], Literal[0]] = None,
        ignore_https_errors: bool = None,
        java_script_enabled: bool = None,
        bypass_csp: bool = None,
        user_agent: str = None,
        locale: str = None,
        timezone_id: str = None,
        geolocation: "Geolocation" = None,
        permissions: typing.List[str] = None,
        extra_http_headers: typing.Union[typing.Dict[str, str]] = None,
        offline: bool = None,
        http_credentials: typing.Union[typing.Tuple[str, str]] = None,
        device_scale_factor: float = None,
        is_mobile: bool = None,
        has_touch: bool = None,
        color_scheme: Literal["dark", "light", "no-preference"] = None,
        accept_downloads: bool = None,
        default_browser_type: str = None,
        proxy: "ProxySettings" = None,
        record_har_path: typing.Union[str, pathlib.Path] = None,
        record_har_omit_content: bool = None,
        record_video_dir: typing.Union[str, pathlib.Path] = None,
        record_video_size: typing.Union[typing.Tuple[int, int]] = None,
        storage_state: typing.Union["StorageState", str, pathlib.Path] = None,
    ) -> "Page":
        """Browser.new_page

        Creates a new page in a new browser context. Closing this page will close the context as well.

        This is a convenience API that should only be used for the single-page scenarios and short snippets. Production code and
        testing frameworks should explicitly create `browser.new_context()` followed by the
        `browser_context.new_page()` to control their exact life times.

        Parameters
        ----------
        viewport : Union["0", typing.Tuple[int, int], NoneType]
            Sets a consistent viewport for each page. Defaults to an 1280x720 viewport. `null` disables the default viewport.
        ignore_https_errors : Union[bool, NoneType]
            Whether to ignore HTTPS errors during navigation. Defaults to `false`.
        java_script_enabled : Union[bool, NoneType]
            Whether or not to enable JavaScript in the context. Defaults to `true`.
        bypass_csp : Union[bool, NoneType]
            Toggles bypassing page's Content-Security-Policy.
        user_agent : Union[str, NoneType]
            Specific user agent to use in this context.
        locale : Union[str, NoneType]
            Specify user locale, for example `en-GB`, `de-DE`, etc. Locale will affect `navigator.language` value, `Accept-Language`
            request header value as well as number and date formatting rules.
        timezone_id : Union[str, NoneType]
            Changes the timezone of the context. See
            [ICU's metaZones.txt](https://cs.chromium.org/chromium/src/third_party/icu/source/data/misc/metaZones.txt?rcl=faee8bc70570192d82d2978a71e2a615788597d1)
            for a list of supported timezone IDs.
        geolocation : Union[{latitude: float, longitude: float, accuracy: Union[float, NoneType]}, NoneType]
        permissions : Union[List[str], NoneType]
            A list of permissions to grant to all pages in this context. See `browser_context.grant_permissions()` for more
            details.
        extra_http_headers : Union[Dict[str, str], NoneType]
            An object containing additional HTTP headers to be sent with every request. All header values must be strings.
        offline : Union[bool, NoneType]
            Whether to emulate network being offline. Defaults to `false`.
        http_credentials : Union[typing.Tuple[str, str], NoneType]
            Credentials for [HTTP authentication](https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication).
        device_scale_factor : Union[float, NoneType]
            Specify device scale factor (can be thought of as dpr). Defaults to `1`.
        is_mobile : Union[bool, NoneType]
            Whether the `meta viewport` tag is taken into account and touch events are enabled. Defaults to `false`. Not supported
            in Firefox.
        has_touch : Union[bool, NoneType]
            Specifies if viewport supports touch events. Defaults to false.
        color_scheme : Union["dark", "light", "no-preference", NoneType]
            Emulates `'prefers-colors-scheme'` media feature, supported values are `'light'`, `'dark'`, `'no-preference'`. See
            `page.emulate_media()` for more details. Defaults to '`light`'.
        accept_downloads : Union[bool, NoneType]
            Whether to automatically download all the attachments. Defaults to `false` where all the downloads are canceled.
        proxy : Union[{server: str, bypass: Union[str, NoneType], username: Union[str, NoneType], password: Union[str, NoneType]}, NoneType]
            Network proxy settings to use with this context. Note that browser needs to be launched with the global proxy for this
            option to work. If all contexts override the proxy, global proxy will be never used and can be any string, for example
            `launch({ proxy: { server: 'per-context' } })`.
        record_har_path : Union[pathlib.Path, str, NoneType]
            Path on the filesystem to write the HAR file to.
        record_har_omit_content : Union[bool, NoneType]
            Optional setting to control whether to omit request content from the HAR. Defaults to `false`.
        record_video_dir : Union[pathlib.Path, str, NoneType]
            Path to the directory to put videos into.
        record_video_size : Union[typing.Tuple[int, int], NoneType]
            Optional dimensions of the recorded videos. If not specified the size will be equal to `viewport`. If `viewport` is not
            configured explicitly the video size defaults to 1280x720. Actual picture of each page will be scaled down if necessary
            to fit the specified size.
        storage_state : Union[pathlib.Path, str, {cookies: Union[List[{name: str, value: str, url: Union[str, NoneType], domain: Union[str, NoneType], path: Union[str, NoneType], expires: Union[float, NoneType], httpOnly: Union[bool, NoneType], secure: Union[bool, NoneType], sameSite: Union["Strict", "Lax", "None", NoneType]}], NoneType], origins: Union[List[Dict], NoneType]}, NoneType]
            Populates context with given storage state. This method can be used to initialize context with logged-in information
            obtained via `browser_context.storage_state()`. Either a path to the file with saved storage, or an object with
            the following fields:

        Returns
        -------
        Page
        """

        try:
            log_api("=> browser.new_page started")
            result = mapping.from_impl(
                self._sync(
                    self._impl_obj.new_page(
                        viewport=viewport,
                        ignoreHTTPSErrors=ignore_https_errors,
                        javaScriptEnabled=java_script_enabled,
                        bypassCSP=bypass_csp,
                        userAgent=user_agent,
                        locale=locale,
                        timezoneId=timezone_id,
                        geolocation=geolocation,
                        permissions=permissions,
                        extraHTTPHeaders=mapping.to_impl(extra_http_headers),
                        offline=offline,
                        httpCredentials=http_credentials,
                        deviceScaleFactor=device_scale_factor,
                        isMobile=is_mobile,
                        hasTouch=has_touch,
                        colorScheme=color_scheme,
                        acceptDownloads=accept_downloads,
                        defaultBrowserType=default_browser_type,
                        proxy=proxy,
                        recordHarPath=record_har_path,
                        recordHarOmitContent=record_har_omit_content,
                        recordVideoDir=record_video_dir,
                        recordVideoSize=record_video_size,
                        storageState=storage_state,
                    )
                )
            )
            log_api("<= browser.new_page succeded")
            return result
        except Exception as e:
            log_api("<= browser.new_page failed")
            raise e

    def close(self) -> NoneType:
        """Browser.close

        In case this browser is obtained using `browser_type.launch()`, closes the browser and all of its pages (if any
        were opened).

        In case this browser is obtained using `browser_type.connect()`, clears all created contexts belonging to this
        browser and disconnects from the browser server.

        The `Browser` object itself is considered to be disposed and cannot be used anymore.
        """

        try:
            log_api("=> browser.close started")
            result = mapping.from_maybe_impl(self._sync(self._impl_obj.close()))
            log_api("<= browser.close succeded")
            return result
        except Exception as e:
            log_api("<= browser.close failed")
            raise e


mapping.register(BrowserImpl, Browser)


class BrowserType(SyncBase):
    def __init__(self, obj: BrowserTypeImpl):
        super().__init__(obj)

    @property
    def name(self) -> str:
        """BrowserType.name

        Returns browser name. For example: `'chromium'`, `'webkit'` or `'firefox'`.

        Returns
        -------
        str
        """
        return mapping.from_maybe_impl(self._impl_obj.name)

    @property
    def executable_path(self) -> str:
        """BrowserType.executable_path

        A path where Playwright expects to find a bundled browser executable.

        Returns
        -------
        str
        """
        return mapping.from_maybe_impl(self._impl_obj.executable_path)

    def launch(
        self,
        executable_path: typing.Union[str, pathlib.Path] = None,
        args: typing.List[str] = None,
        ignore_default_args: typing.Union[bool, typing.List[str]] = None,
        handle_sigint: bool = None,
        handle_sigterm: bool = None,
        handle_sighup: bool = None,
        timeout: float = None,
        env: typing.Union[typing.Dict[str, typing.Union[str, float, bool]]] = None,
        headless: bool = None,
        devtools: bool = None,
        proxy: "ProxySettings" = None,
        downloads_path: typing.Union[str, pathlib.Path] = None,
        slow_mo: float = None,
        chromium_sandbox: bool = None,
        firefox_user_prefs: typing.Union[
            typing.Dict[str, typing.Union[str, float, bool]]
        ] = None,
    ) -> "Browser":
        """BrowserType.launch

        Returns the browser instance.

        You can use `ignoreDefaultArgs` to filter out `--mute-audio` from default arguments:

        > **Chromium-only** Playwright can also be used to control the Chrome browser, but it works best with the version of
        Chromium it is bundled with. There is no guarantee it will work with any other version. Use `executablePath` option with
        extreme caution.
        >
        > If Google Chrome (rather than Chromium) is preferred, a
        [Chrome Canary](https://www.google.com/chrome/browser/canary.html) or
        [Dev Channel](https://www.chromium.org/getting-involved/dev-channel) build is suggested.
        >
        > In `browser_type.launch()` above, any mention of Chromium also applies to Chrome.
        >
        > See [`this article`](https://www.howtogeek.com/202825/what%E2%80%99s-the-difference-between-chromium-and-chrome/) for
        a description of the differences between Chromium and Chrome.
        [`This article`](https://chromium.googlesource.com/chromium/src/+/lkgr/docs/chromium_browser_vs_google_chrome.md)
        describes some differences for Linux users.

        Parameters
        ----------
        executable_path : Union[pathlib.Path, str, NoneType]
            Path to a browser executable to run instead of the bundled one. If `executablePath` is a relative path, then it is
            resolved relative to the current working directory. Note that Playwright only works with the bundled Chromium, Firefox
            or WebKit, use at your own risk.
        args : Union[List[str], NoneType]
            Additional arguments to pass to the browser instance. The list of Chromium flags can be found
            [here](http://peter.sh/experiments/chromium-command-line-switches/).
        ignore_default_args : Union[List[str], bool, NoneType]
            If `true`, Playwright does not pass its own configurations args and only uses the ones from `args`. If an array is
            given, then filters out the given default arguments. Dangerous option; use with care. Defaults to `false`.
        handle_sigint : Union[bool, NoneType]
            Close the browser process on Ctrl-C. Defaults to `true`.
        handle_sigterm : Union[bool, NoneType]
            Close the browser process on SIGTERM. Defaults to `true`.
        handle_sighup : Union[bool, NoneType]
            Close the browser process on SIGHUP. Defaults to `true`.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds to wait for the browser instance to start. Defaults to `30000` (30 seconds). Pass `0` to
            disable timeout.
        env : Union[Dict[str, Union[bool, float, str]], NoneType]
            Specify environment variables that will be visible to the browser. Defaults to `process.env`.
        headless : Union[bool, NoneType]
            Whether to run browser in headless mode. More details for
            [Chromium](https://developers.google.com/web/updates/2017/04/headless-chrome) and
            [Firefox](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Headless_mode). Defaults to `true` unless the
            `devtools` option is `true`.
        devtools : Union[bool, NoneType]
            **Chromium-only** Whether to auto-open a Developer Tools panel for each tab. If this option is `true`, the `headless`
            option will be set `false`.
        proxy : Union[{server: str, bypass: Union[str, NoneType], username: Union[str, NoneType], password: Union[str, NoneType]}, NoneType]
            Network proxy settings.
        downloads_path : Union[pathlib.Path, str, NoneType]
            If specified, accepted downloads are downloaded into this directory. Otherwise, temporary directory is created and is
            deleted when browser is closed.
        slow_mo : Union[float, NoneType]
            Slows down Playwright operations by the specified amount of milliseconds. Useful so that you can see what is going on.
        chromium_sandbox : Union[bool, NoneType]
            Enable Chromium sandboxing. Defaults to `false`.
        firefox_user_prefs : Union[Dict[str, Union[bool, float, str]], NoneType]
            Firefox user preferences. Learn more about the Firefox user preferences at
            [`about:config`](https://support.mozilla.org/en-US/kb/about-config-editor-firefox).

        Returns
        -------
        Browser
        """

        try:
            log_api("=> browser_type.launch started")
            result = mapping.from_impl(
                self._sync(
                    self._impl_obj.launch(
                        executablePath=executable_path,
                        args=args,
                        ignoreDefaultArgs=ignore_default_args,
                        handleSIGINT=handle_sigint,
                        handleSIGTERM=handle_sigterm,
                        handleSIGHUP=handle_sighup,
                        timeout=timeout,
                        env=mapping.to_impl(env),
                        headless=headless,
                        devtools=devtools,
                        proxy=proxy,
                        downloadsPath=downloads_path,
                        slowMo=slow_mo,
                        chromiumSandbox=chromium_sandbox,
                        firefoxUserPrefs=mapping.to_impl(firefox_user_prefs),
                    )
                )
            )
            log_api("<= browser_type.launch succeded")
            return result
        except Exception as e:
            log_api("<= browser_type.launch failed")
            raise e

    def launch_persistent_context(
        self,
        user_data_dir: typing.Union[str, pathlib.Path],
        executable_path: typing.Union[str, pathlib.Path] = None,
        args: typing.List[str] = None,
        ignore_default_args: typing.Union[bool, typing.List[str]] = None,
        handle_sigint: bool = None,
        handle_sigterm: bool = None,
        handle_sighup: bool = None,
        timeout: float = None,
        env: typing.Union[typing.Dict[str, typing.Union[str, float, bool]]] = None,
        headless: bool = None,
        devtools: bool = None,
        proxy: "ProxySettings" = None,
        downloads_path: typing.Union[str, pathlib.Path] = None,
        slow_mo: float = None,
        viewport: typing.Union[typing.Tuple[int, int], Literal[0]] = None,
        ignore_https_errors: bool = None,
        java_script_enabled: bool = None,
        bypass_csp: bool = None,
        user_agent: str = None,
        locale: str = None,
        timezone_id: str = None,
        geolocation: "Geolocation" = None,
        permissions: typing.List[str] = None,
        extra_http_headers: typing.Union[typing.Dict[str, str]] = None,
        offline: bool = None,
        http_credentials: typing.Union[typing.Tuple[str, str]] = None,
        device_scale_factor: float = None,
        is_mobile: bool = None,
        has_touch: bool = None,
        color_scheme: Literal["dark", "light", "no-preference"] = None,
        accept_downloads: bool = None,
        chromium_sandbox: bool = None,
        record_har_path: typing.Union[str, pathlib.Path] = None,
        record_har_omit_content: bool = None,
        record_video_dir: typing.Union[str, pathlib.Path] = None,
        record_video_size: typing.Union[typing.Tuple[int, int]] = None,
    ) -> "BrowserContext":
        """BrowserType.launch_persistent_context

        Returns the persistent browser context instance.

        Launches browser that uses persistent storage located at `userDataDir` and returns the only context. Closing this
        context will automatically close the browser.

        Parameters
        ----------
        user_data_dir : Union[pathlib.Path, str]
            Path to a User Data Directory, which stores browser session data like cookies and local storage. More details for
            [Chromium](https://chromium.googlesource.com/chromium/src/+/master/docs/user_data_dir.md) and
            [Firefox](https://developer.mozilla.org/en-US/docs/Mozilla/Command_Line_Options#User_Profile).
        executable_path : Union[pathlib.Path, str, NoneType]
            Path to a browser executable to run instead of the bundled one. If `executablePath` is a relative path, then it is
            resolved relative to the current working directory. **BEWARE**: Playwright is only guaranteed to work with the bundled
            Chromium, Firefox or WebKit, use at your own risk.
        args : Union[List[str], NoneType]
            Additional arguments to pass to the browser instance. The list of Chromium flags can be found
            [here](http://peter.sh/experiments/chromium-command-line-switches/).
        ignore_default_args : Union[List[str], bool, NoneType]
            If `true`, then do not use any of the default arguments. If an array is given, then filter out the given default
            arguments. Dangerous option; use with care. Defaults to `false`.
        handle_sigint : Union[bool, NoneType]
            Close the browser process on Ctrl-C. Defaults to `true`.
        handle_sigterm : Union[bool, NoneType]
            Close the browser process on SIGTERM. Defaults to `true`.
        handle_sighup : Union[bool, NoneType]
            Close the browser process on SIGHUP. Defaults to `true`.
        timeout : Union[float, NoneType]
            Maximum time in milliseconds to wait for the browser instance to start. Defaults to `30000` (30 seconds). Pass `0` to
            disable timeout.
        env : Union[Dict[str, Union[bool, float, str]], NoneType]
            Specify environment variables that will be visible to the browser. Defaults to `process.env`.
        headless : Union[bool, NoneType]
            Whether to run browser in headless mode. More details for
            [Chromium](https://developers.google.com/web/updates/2017/04/headless-chrome) and
            [Firefox](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Headless_mode). Defaults to `true` unless the
            `devtools` option is `true`.
        devtools : Union[bool, NoneType]
            **Chromium-only** Whether to auto-open a Developer Tools panel for each tab. If this option is `true`, the `headless`
            option will be set `false`.
        proxy : Union[{server: str, bypass: Union[str, NoneType], username: Union[str, NoneType], password: Union[str, NoneType]}, NoneType]
            Network proxy settings.
        downloads_path : Union[pathlib.Path, str, NoneType]
            If specified, accepted downloads are downloaded into this directory. Otherwise, temporary directory is created and is
            deleted when browser is closed.
        slow_mo : Union[float, NoneType]
            Slows down Playwright operations by the specified amount of milliseconds. Useful so that you can see what is going on.
            Defaults to 0.
        viewport : Union["0", typing.Tuple[int, int], NoneType]
            Sets a consistent viewport for each page. Defaults to an 1280x720 viewport. `null` disables the default viewport.
        ignore_https_errors : Union[bool, NoneType]
            Whether to ignore HTTPS errors during navigation. Defaults to `false`.
        java_script_enabled : Union[bool, NoneType]
            Whether or not to enable JavaScript in the context. Defaults to `true`.
        bypass_csp : Union[bool, NoneType]
            Toggles bypassing page's Content-Security-Policy.
        user_agent : Union[str, NoneType]
            Specific user agent to use in this context.
        locale : Union[str, NoneType]
            Specify user locale, for example `en-GB`, `de-DE`, etc. Locale will affect `navigator.language` value, `Accept-Language`
            request header value as well as number and date formatting rules.
        timezone_id : Union[str, NoneType]
            Changes the timezone of the context. See
            [ICU's metaZones.txt](https://cs.chromium.org/chromium/src/third_party/icu/source/data/misc/metaZones.txt?rcl=faee8bc70570192d82d2978a71e2a615788597d1)
            for a list of supported timezone IDs.
        geolocation : Union[{latitude: float, longitude: float, accuracy: Union[float, NoneType]}, NoneType]
        permissions : Union[List[str], NoneType]
            A list of permissions to grant to all pages in this context. See `browser_context.grant_permissions()` for more
            details.
        extra_http_headers : Union[Dict[str, str], NoneType]
            An object containing additional HTTP headers to be sent with every request. All header values must be strings.
        offline : Union[bool, NoneType]
            Whether to emulate network being offline. Defaults to `false`.
        http_credentials : Union[typing.Tuple[str, str], NoneType]
            Credentials for [HTTP authentication](https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication).
        device_scale_factor : Union[float, NoneType]
            Specify device scale factor (can be thought of as dpr). Defaults to `1`.
        is_mobile : Union[bool, NoneType]
            Whether the `meta viewport` tag is taken into account and touch events are enabled. Defaults to `false`. Not supported
            in Firefox.
        has_touch : Union[bool, NoneType]
            Specifies if viewport supports touch events. Defaults to false.
        color_scheme : Union["dark", "light", "no-preference", NoneType]
            Emulates `'prefers-colors-scheme'` media feature, supported values are `'light'`, `'dark'`, `'no-preference'`. See
            `page.emulate_media()` for more details. Defaults to '`light`'.
        accept_downloads : Union[bool, NoneType]
            Whether to automatically download all the attachments. Defaults to `false` where all the downloads are canceled.
        chromium_sandbox : Union[bool, NoneType]
            Enable Chromium sandboxing. Defaults to `true`.
        record_har_path : Union[pathlib.Path, str, NoneType]
            Path on the filesystem to write the HAR file to.
        record_har_omit_content : Union[bool, NoneType]
            Optional setting to control whether to omit request content from the HAR. Defaults to `false`.
        record_video_dir : Union[pathlib.Path, str, NoneType]
            Path to the directory to put videos into.
        record_video_size : Union[typing.Tuple[int, int], NoneType]
            Optional dimensions of the recorded videos. If not specified the size will be equal to `viewport`. If `viewport` is not
            configured explicitly the video size defaults to 1280x720. Actual picture of each page will be scaled down if necessary
            to fit the specified size.

        Returns
        -------
        BrowserContext
        """

        try:
            log_api("=> browser_type.launch_persistent_context started")
            result = mapping.from_impl(
                self._sync(
                    self._impl_obj.launch_persistent_context(
                        userDataDir=user_data_dir,
                        executablePath=executable_path,
                        args=args,
                        ignoreDefaultArgs=ignore_default_args,
                        handleSIGINT=handle_sigint,
                        handleSIGTERM=handle_sigterm,
                        handleSIGHUP=handle_sighup,
                        timeout=timeout,
                        env=mapping.to_impl(env),
                        headless=headless,
                        devtools=devtools,
                        proxy=proxy,
                        downloadsPath=downloads_path,
                        slowMo=slow_mo,
                        viewport=viewport,
                        ignoreHTTPSErrors=ignore_https_errors,
                        javaScriptEnabled=java_script_enabled,
                        bypassCSP=bypass_csp,
                        userAgent=user_agent,
                        locale=locale,
                        timezoneId=timezone_id,
                        geolocation=geolocation,
                        permissions=permissions,
                        extraHTTPHeaders=mapping.to_impl(extra_http_headers),
                        offline=offline,
                        httpCredentials=http_credentials,
                        deviceScaleFactor=device_scale_factor,
                        isMobile=is_mobile,
                        hasTouch=has_touch,
                        colorScheme=color_scheme,
                        acceptDownloads=accept_downloads,
                        chromiumSandbox=chromium_sandbox,
                        recordHarPath=record_har_path,
                        recordHarOmitContent=record_har_omit_content,
                        recordVideoDir=record_video_dir,
                        recordVideoSize=record_video_size,
                    )
                )
            )
            log_api("<= browser_type.launch_persistent_context succeded")
            return result
        except Exception as e:
            log_api("<= browser_type.launch_persistent_context failed")
            raise e


mapping.register(BrowserTypeImpl, BrowserType)


class Playwright(SyncBase):
    def __init__(self, obj: PlaywrightImpl):
        super().__init__(obj)

    @property
    def devices(self) -> typing.Dict[str, "DeviceDescriptor"]:
        """Playwright.devices

        Returns a list of devices to be used with `browser.new_context()` or `browser.new_page()`. Actual list of
        devices can be found in
        [src/server/deviceDescriptors.ts](https://github.com/Microsoft/playwright/blob/master/src/server/deviceDescriptors.ts).

        Returns
        -------
        Dict[str, {user_agent: Union[str, NoneType], viewport: Union[typing.Tuple[int, int], NoneType], device_scale_factor: Union[int, NoneType], is_mobile: Union[bool, NoneType], has_touch: Union[bool, NoneType]}]
        """
        return mapping.from_impl_dict(self._impl_obj.devices)

    @property
    def selectors(self) -> "Selectors":
        """Playwright.selectors

        Selectors can be used to install custom selector engines. See
        [Working with selectors](./selectors.md#working-with-selectors) for more information.

        Returns
        -------
        Selectors
        """
        return mapping.from_impl(self._impl_obj.selectors)

    @property
    def chromium(self) -> "BrowserType":
        """Playwright.chromium

        This object can be used to launch or connect to Chromium, returning instances of `ChromiumBrowser`.

        Returns
        -------
        BrowserType
        """
        return mapping.from_impl(self._impl_obj.chromium)

    @property
    def firefox(self) -> "BrowserType":
        """Playwright.firefox

        This object can be used to launch or connect to Firefox, returning instances of `FirefoxBrowser`.

        Returns
        -------
        BrowserType
        """
        return mapping.from_impl(self._impl_obj.firefox)

    @property
    def webkit(self) -> "BrowserType":
        """Playwright.webkit

        This object can be used to launch or connect to WebKit, returning instances of `WebKitBrowser`.

        Returns
        -------
        BrowserType
        """
        return mapping.from_impl(self._impl_obj.webkit)

    def stop(self) -> NoneType:

        try:
            log_api("=> playwright.stop started")
            result = mapping.from_maybe_impl(self._impl_obj.stop())
            log_api("<= playwright.stop succeded")
            return result
        except Exception as e:
            log_api("<= playwright.stop failed")
            raise e


mapping.register(PlaywrightImpl, Playwright)

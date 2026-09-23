# ========= Copyright 2023-2026 @ CAMEL-AI.org. All Rights Reserved. =========
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ========= Copyright 2023-2026 @ CAMEL-AI.org. All Rights Reserved. =========
from abc import ABC, abstractmethod
from typing import List, Optional, Tuple

from camel.messages import BaseMessage


class BaseTerminator(ABC):
    r"""Base class for terminators."""

    def __init__(self, *args, **kwargs) -> None:
        r"""Initialize shared termination state.

        Args:
            *args (Any): Positional arguments accepted by subclasses.
            **kwargs (Any): Keyword arguments accepted by subclasses.
        """
        self._terminated: bool = False
        self._termination_reason: Optional[str] = None

    @abstractmethod
    def is_terminated(self, *args, **kwargs) -> Tuple[bool, Optional[str]]:
        r"""Check whether the termination condition has been met.

        Args:
            *args (Any): Positional values required by the implementation.
            **kwargs (Any): Keyword values required by the implementation.

        Returns:
            Tuple[bool, Optional[str]]: Termination status and its reason.
        """
        pass

    @abstractmethod
    def reset(self):
        r"""Reset the terminator so it can evaluate a new conversation."""
        pass


class ResponseTerminator(BaseTerminator):
    r"""A terminator that terminates the conversation based on the response."""

    @abstractmethod
    def is_terminated(
        self, messages: List[BaseMessage]
    ) -> Tuple[bool, Optional[str]]:
        r"""Check a response for the implementation's stop condition.

        Args:
            messages (List[BaseMessage]): Messages in the current response.

        Returns:
            Tuple[bool, Optional[str]]: Termination status and its reason.
        """
        pass

    @abstractmethod
    def reset(self):
        r"""Reset response-specific termination state."""
        pass

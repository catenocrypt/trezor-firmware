# Automatically generated by pb2py
# fmt: off
# isort:skip_file
import protobuf as p

from .CardanoTokenType import CardanoTokenType

if __debug__:
    try:
        from typing import Dict, List, Optional  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class CardanoAssetGroupType(p.MessageType):

    def __init__(
        self,
        *,
        policy_id: bytes,
        tokens: Optional[List[CardanoTokenType]] = None,
    ) -> None:
        self.tokens = tokens if tokens is not None else []
        self.policy_id = policy_id

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('policy_id', p.BytesType, p.FLAG_REQUIRED),
            2: ('tokens', CardanoTokenType, p.FLAG_REPEATED),
        }

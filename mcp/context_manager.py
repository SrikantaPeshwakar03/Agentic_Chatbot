import uuid
from typing import Dict, Any, List

class Message:
    def __init__(self, sender: str, receiver: str, msg_type: str, payload: Dict[str, Any], trace_id: str = None):
        self.sender = sender
        self.receiver = receiver
        self.type = msg_type
        self.payload = payload
        self.trace_id = trace_id or str(uuid.uuid4())

    def to_dict(self):
        return {
            "sender": self.sender,
            "receiver": self.receiver,
            "type": self.type,
            "trace_id": self.trace_id,
            "payload": self.payload
        }

    def __repr__(self):
        return f"[{self.type}] From: {self.sender} → {self.receiver} | Payload: {self.payload}"

class ContextManager:
    def __init__(self):
        self.messages: List[Message] = []

    def send(self, message: Message):
        self.messages.append(message)

    def get_trace(self, trace_id: str):
        return [msg.to_dict() for msg in self.messages if msg.trace_id == trace_id]

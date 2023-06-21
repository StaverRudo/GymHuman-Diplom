from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        if self.scope["user"].is_anonymous:
            # Если пользователь не авторизован, закрываем соединение
            await self.close()
        else:
            # Подключаемся к комнате чата
            self.room_name = "default"
            self.room_group_name = f"chat_{self.room_name}"

            await self.channel_layer.group_add(self.room_group_name, self.channel_name)
            await self.accept()

    async def disconnect(self, close_code):
        # Отключаемся от комнаты чата
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        # Получаем сообщение от пользователя и отправляем его всем в комнате
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": text_data,
                "user": self.scope["user"].username,
            },
        )

    async def chat_message(self, event):
        # Отправляем сообщение всем в комнате
        await self.send(
            text_data=event["message"],
        )

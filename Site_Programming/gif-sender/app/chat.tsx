"use client"
import { useState } from 'react';

const Chat = () => {
    const [messages, setMessages] = useState<{ text: string; id: number }[]>([]);
    const [input, setInput] = useState('');

    const handleSend = () => {
        if (input.trim()) {
            setMessages([...messages, { text: input, id: Date.now() }]);
            setInput('');
        }
    };

    const handleKeyPress = (e: React.KeyboardEvent) => {
        if (e.key === 'Enter') handleSend();
    };

    return (
        <div className="flex flex-col w-full max-w-md mx-auto p-4">
            <div className="flex-grow overflow-y-auto bg-gray-100 rounded-lg p-4">
                {messages.map((msg) => (
                    <div key={msg.id} className="p-2 my-2 bg-blue-400 rounded">
                        {msg.text}
                    </div>
                ))}
            </div>
            <div className="flex items-center mt-4">
                <input
                    type="text"
                    value={input}
                    onChange={(e) => setInput(e.target.value)}
                    onKeyDown={handleKeyPress}
                    placeholder="Type a message"
                    className="flex-grow p-2 border text-black bg-gray-100 rounded-l"
                />
                <button
                    onClick={handleSend}
                    className="px-4 py-2 bg-blue-500 text-white-500 rounded-r"
                >
                    Send
                </button>
            </div>
        </div>
    );
};

export default Chat;
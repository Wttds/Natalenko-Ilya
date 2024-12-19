import Image from "next/image";
import Chat from '@/app/chat';

export default function Page() {
    return (
        <main className="flex justify-center items-center h-screen bg-gray-50">
            <Chat />
        </main>
    );
}

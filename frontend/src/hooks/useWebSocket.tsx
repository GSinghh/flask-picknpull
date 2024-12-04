import { useState, useEffect } from "react";
import { io, Socket } from "socket.io-client";

const SOCKET_SERVER_URL = "http://127.0.0.1:5000";

export const useWebSocket = () => {
    const [socket, setSocket] = useState<Socket | null>(null);
    useEffect(() => {
        const socket = io("http://127.0.0.1:5000", {
            transports: ["websocket", "polling"],
        }); // Replace with your Flask server URL

        socket.on("connect", () => {
            console.log("Connected to server");
        });

        // Handle other events here

        return () => {
            socket.disconnect();
        };
    }, []);
    return socket;
};

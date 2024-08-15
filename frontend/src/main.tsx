import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import { BrowserRouter as Router } from "react-router-dom";
import "./index.css";
import Navbar from "./components/Navbar";
import Sidebar from "./components/Sidebar";

createRoot(document.getElementById("root")!).render(
    <StrictMode>
        <Router>
            <div className="container">
                <Sidebar />
                <Navbar />
            </div>
        </Router>
    </StrictMode>
);

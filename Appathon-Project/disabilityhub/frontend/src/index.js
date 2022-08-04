import React from "react";
import { App } from "./components/App";
import { StrictMode } from "react";
import ReactDOM from "react-dom/client";

const root = ReactDOM.createRoot(document.getElementById("app"));
root.render(
    <StrictMode>
        <App />
    </StrictMode>
);
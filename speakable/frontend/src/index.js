import React from "react";
import { Home } from "./components/Home"
import { StrictMode } from "react";
import ReactDOM from "react-dom/client";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
    <StrictMode>
        <Home />
    </StrictMode>
);
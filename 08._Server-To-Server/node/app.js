import express from "express";

const app = express();

app.get("/requestFastAPI", async (req, res) => {
    const response = await fetch("http://127.0.0.1:8000/fastapiData");
    const result = await response.json();
    res.send({ data: result });
});

app.get("/expressData", (req, res) => {
    res.send({ message: "isRunning" });
});


const PORT = 8080;
app.listen(PORT, () => console.log("Server is running on port", PORT));

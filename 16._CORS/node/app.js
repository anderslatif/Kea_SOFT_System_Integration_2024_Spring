import express from "express";
const app = express();


app.get("/timestamp", (req, res) => {
    res.send({ time: new Date() });
});

const PORT = process.env.PORT ?? 8080;
app.listen(PORT, () => console.log("Server is running on port", 8080));

import express from "express";

const app = express();

            // request, response
app.get("/", (req, res) => {
    res.send({ message: "Hello" });
});

app.get("/otherRoute", (req, res) => {
    res.send({ message: "This is the other route" });
});

app.post("/postrequest", (req, res) => {
    res.send({ message: "You made a post request" });
});

const PORT = 8080;
app.listen(PORT, () => console.log("Server is running on port", PORT));

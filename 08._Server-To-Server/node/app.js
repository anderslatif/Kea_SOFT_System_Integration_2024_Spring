import express from "express";

const app = express();

app.get("/requestFastAPI", (req, res) => {
    
    res.send({ });
});


const PORT = 8080;
app.listen(PORT, () => console.log("Server is running on port", PORT));

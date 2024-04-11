import express from "express";
const app = express();

app.use(express.urlencoded({ extended: true }));

import multer from "multer";
// const upload = multer({ dest: "./uploads" });

const storage = multer.diskStorage({
    destination: (req, file, cb) => {
        cb(null, './uploads');
    },
    filename: (req, file, cb) => {
        const uniquePrefix = Date.now() + '-' + Math.round(Math.random() * 1E9);
        const uniqueFileName = `${uniquePrefix}__${file.originalname}`;

        cb(null, uniqueFileName);
    }
});

function fileFilter(req, file, cb) {
    const allowedTypes = ['image/jpeg', 'image/svg', 'image/png'];

    if (!allowedTypes.includes(file.mimetype)) {
        cb(new Error("File type not allowed: " + file.mimetype), false);
    } else {
        cb(null, true);
    }
}

const upload = multer({ 
    storage,
    limits: {
        fileSize: 10 * 1024 * 1024 // 10MB
    }, 
    fileFilter
});

app.post("/form", (req, res) => {
    console.log(req.body);
    delete req.body.password;
    res.send(req.body);
});

app.post('/fileform', upload.single('file'), (req, res) => {
    console.log(req.body);
    res.send({ });
});


const PORT = process.env.PORT ?? 8080;
app.listen(PORT, () => console.log("Server is running on port", PORT));

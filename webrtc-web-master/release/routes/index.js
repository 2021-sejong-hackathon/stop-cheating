const express = require('express');
const router = express.Router();

// 라우터 파일 가져오기
router.get('/hi', (req, res) => {
    res.sendFile(__dirname + '/index.html');
});

// 라우터 파일 등록하기



module.exports = router;
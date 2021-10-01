const imageUpload = document.getElementById('imageUpload');
const verifyBtn = document.getElementById('verify-btn');
const snapshotBtn = document.getElementById('snapshot-btn');

const curUser = 'youngmin';

// load models
Promise.all([
    faceapi.nets.faceRecognitionNet.loadFromUri('/models'),
    faceapi.nets.faceLandmark68Net.loadFromUri('/models'),
    faceapi.nets.ssdMobilenetv1.loadFromUri('/models')
]).then(start)

// attach webcam
Webcam.set({
    width: 350,
    height: 350,
    image_format: 'jpeg',
    jpeg_quality: 90
})

Webcam.attach("#camera")

let captureImg;
// snapshot function
function take_snapshot() {
    Webcam.snap(function (data_uri) {
        captureImg = document.getElementById('captureImg');
        const image = document.createElement('img');
        image.setAttribute('id', 'snapedImg');
        image.setAttribute('src', data_uri)
        captureImg.appendChild(image);
    })
}

async function start() {

    snapshotBtn.classList.add('active')
    verifyBtn.classList.add('active');
    snapshotBtn.disabled = false;
    verifyBtn.disabled = false;

    const labeledFaceDescriptors = await loadLabeledImages()

    const faceMatcher = new faceapi.FaceMatcher(labeledFaceDescriptors, 0.6)

    verifyBtn.onclick = async () => {

        // Webcam.snap(function(data_uri) {
        //   document.getElementById('results').innerHTML =
        //   '<img id="snapedImg" style="display:none" src="'+data_uri+'"/>';
        // })

        const image = document.getElementById('snapedImg')

        const canvas = faceapi.createCanvasFromMedia(image)

        const displaySize = {width: image.width, height: image.height}
        faceapi.matchDimensions(canvas, displaySize)

        const detections = await faceapi.detectAllFaces(image).withFaceLandmarks().withFaceDescriptors()
        const resizedDetections = faceapi.resizeResults(detections, displaySize)
        const results = resizedDetections.map(d => faceMatcher.findBestMatch(d.descriptor)) // 60%의 confidence인 label로 매칭됨.

        snapedPerson = results.toString().split(' ')[0]

        const resultsString = document.getElementById('results');

        if (snapedPerson == curUser) {
            const link = document.createElement('a');
            link.innerText = "테스트로 이동하세요."
            link.href = '/test'

            resultsString.appendChild(link);
        } else {
            resultsString.innerText = "인증에 실패하였습니다.";
            captureImg.innerHTML = ""
        }
    }
}

function loadLabeledImages() {
    const labels = ['seojun', 'sky', 'youngmin']

    return Promise.all(
        labels.map(async label => {
            const descriptions = []
            for (let i = 1; i <= 3; i++) {
                const img = await faceapi.fetchImage(`https://raw.githubusercontent.com/MartinusChoi/OpenCV4/main/img/${label}/${i}.jpg`)
                const detections = await faceapi.detectSingleFace(img).withFaceLandmarks().withFaceDescriptor()
                descriptions.push(detections.descriptor)
            }

            return new faceapi.LabeledFaceDescriptors(label, descriptions)
        })
    )
}
const imageUpload = document.getElementById('imageUpload')
const verifybtn = document.getElementById('verify')

const curUser = 'youngmin';

// load models
Promise.all([
  faceapi.nets.faceRecognitionNet.loadFromUri('/models'),
  faceapi.nets.faceLandmark68Net.loadFromUri('/models'),
  faceapi.nets.ssdMobilenetv1.loadFromUri('/models')
]).then(start)

// attach webcam
Webcam.set({
  width:350,
  height:350,
  image_format:'jpeg',
  jpeg_quality:90
})
Webcam.attach("#camera")

// snapshot function
function take_snapshot() {
  Webcam.snap(function(data_uri) {
    document.getElementById('results').innerHTML = 
    '<img id="snapedImg" src="'+data_uri+'"/>';
  })
}

async function start() {
  const container = document.createElement('div')
  container.style.position = 'relative'
  document.body.append(container)

  const labeledFaceDescriptors = await loadLabeledImages()

  const faceMatcher = new faceapi.FaceMatcher(labeledFaceDescriptors, 0.6)

  document.body.append('Loaded')

  verifybtn.onclick = async () => {

    // Webcam.snap(function(data_uri) {
    //   document.getElementById('results').innerHTML = 
    //   '<img id="snapedImg" style="display:none" src="'+data_uri+'"/>';
    // })

    const image = document.getElementById('snapedImg')

    container.append(image)
    const canvas = faceapi.createCanvasFromMedia(image)
    container.append(canvas)

    const displaySize = { width: image.width, height: image.height }
    faceapi.matchDimensions(canvas, displaySize)

    const detections = await faceapi.detectAllFaces(image).withFaceLandmarks().withFaceDescriptors()
    const resizedDetections = faceapi.resizeResults(detections, displaySize)
    const results = resizedDetections.map(d => faceMatcher.findBestMatch(d.descriptor)) // 60%의 confidence인 label로 매칭됨.
    
    snapedPerson = results.toString().split(' ')[0]

    if (snapedPerson == curUser) {
      document.body.append("Verify Success!!")
    }
    else {
      document.body.append("Verify Failed!!")
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
        document.body.append('ok')
        const detections = await faceapi.detectSingleFace(img).withFaceLandmarks().withFaceDescriptor()
        descriptions.push(detections.descriptor)
      }

      return new faceapi.LabeledFaceDescriptors(label, descriptions)
    })
  )
}
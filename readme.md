docker build -t lumidora-tts .

docker run -d -p 8080:8080 -v lumidora-tts:/go/src/app/models lumidora-tts

# Push to dockerhub
docker login
docker tag my-image:latest domoskanonos/lumidora-tts
docker push domoskanonos/lumidora-tts




Example Post Call:


http://localhost:8080/api/tts

{
"text": "In einem verschlafenen Dorf, umgeben von majestätischen Bergen, flüsterte eine uralte Eiche Geschichten des Lebens. Ihr mächtiger Stamm trug die Narben der Zeit. Jeden Tag versammelten sich Dorfbewohner um sie und lauschten ihren Erzählungen über vergangene Helden und Abenteuer. Doch an einem nebligen Morgen stand ein Fremder unter der Eiche. Er sprach von fernen Ländern und aufregenden Entdeckungen. Das Dorf wurde lebendig von seinen Worten und verließ die vertraute Routine. Die Eiche schwieg, ihre Geschichten wurden von neuen ersetzt. So entdeckte das Dorf, dass Geschichten nicht nur in den Wurzeln der Vergangenheit, sondern auch in den Ästen der Zukunft schlummerten.",
"voice": "de_DE-thorsten-high.onnx"
}
'use client'

import { useState } from 'react'

const Recorder = async () => {
  const [recorder, setRecorder] = useState<MediaRecorder | null>(null)
  const [audio, setAudio] = useState<string>('')

  const startRecording = async () => {
    /** MediaRecorderを使用して音声データを録音 */
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true })
    const mediaRecorder = new MediaRecorder(stream)
    mediaRecorder.start()
    setRecorder(mediaRecorder)
  }



  return (
    <div>
      <button onClick={startRecording}>Start Recording</button>
      {audio && <audio src={audio} controls />}
    </div>
  )
}

export default Recorder

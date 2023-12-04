import Recorder from './usemedia'
import styles from './page.module.css'

export default function Home(): JSX.Element {
  return (
    <main className={styles.main}>
      <div className={styles.grid}>
        <Recorder />
      </div>
    </main>
  )
}

import NewsComponent from "@/app/ui/news-component"
import {getAllNews} from "@/app/lib/data"
import Link from "next/link";

export default async function Home() {
  const newsData = await getAllNews();
  return (
      <div className="grid grid-rows-[30px_1fr] items-center justify-items-center min-h-screen p-8 pb-20 gap-16 sm:p-20 font-[family-name:var(--font-geist-sans)]">
          <p className="news_header">News page</p>
          <Link href={"/"}>Back</Link>
          <main className="flex flex-col gap-8 row-start-2 items-center sm:items-start">
              <NewsComponent newsData={newsData} isOneNews={false}/>
          </main>
      </div>
  );
}

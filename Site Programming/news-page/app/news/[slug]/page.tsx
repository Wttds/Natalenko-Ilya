import {getNewsById} from "@/app/lib/data";
import NewsComponent from "@/app/ui/news-component";

export default async function Page({params}: {params: {slug: string}}) {
    const { slug } = await params;
    const newsData = await getNewsById(Number(slug));
    const newsArray = newsData ? [newsData] : [];

    return (
        <div className="grid grid-rows-[20px 1fr 20px] items-center justify-items-center min-h-screen p-8 pb-2">
            <main className="fles flex-col gap-8 row-start-2 items-center sm:items-start">
                <NewsComponent newsData={newsArray} isOneNews={true} />
            </main>
        </div>
    )
}
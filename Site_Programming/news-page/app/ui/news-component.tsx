import Link from "next/link";
import { news } from "@prisma/client"

export default async function NewsComponent({newsData, isOneNews} : {newsData: news[], isOneNews: boolean,}) {
    return (
        <div className="grid grid-cols-1 gap-4">
            {newsData.map((elem) => (
                <Link href={`/news/${elem.id}`} key={elem.id} className={"group"}>
                    <div key={elem.id} className={"bg-orange-500 rounded-lg shadow-sm p-6"}>
                        <div className="font-bold">
                            Hello, {elem.title}
                        </div>
                        {isOneNews && (
                            <div>
                                <div>
                                    Date: {elem.date.toDateString()}
                                </div>
                                <div>
                                    Text: {elem.text}
                                </div>
                                <div>
                                    Img: {elem.image}
                                </div>
                            </div>
                        )}
                    </div>
                </Link>
            ))}
        </div>
    );
}

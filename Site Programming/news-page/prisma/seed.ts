import prisma from "../app/lib/db";

async function main() {
    const newsArray = [
        {
            title: "JS learning",
            date: new Date("2024-12-01"),
            text: "Today we've been learning JavaScript.",
            image: "JS Image",
        },
        {
            title: "Prisma learning",
            date: new Date("2024-12-02"),
            text: "Today we've been learning Prisma.",
            image: "Prisma Image",
        },
        {
            title: "Docker learning",
            date: new Date("2024-12-03"),
            text: "Today we've been learning Docker.",
            image: "Docker image",
        },
    ];

    for (const newsData of newsArray) {
        await prisma.news.upsert({
            where: {title: newsData.title},
            update: {
                date: newsData.date,
                text: newsData.text,
                image: newsData.image
            },
            create: {
                title: newsData.title,
                date: newsData.date,
                text: newsData.text,
                image: newsData.image,
            },
        });
        console.log(`Loaded news: ${newsData.title}`);
    }
}

main()
    .then(async () => {
        await prisma.$disconnect();
    })
    .catch(async (e) => {
        console.error(e);
        await prisma.$disconnect();
        process.exit(1);
    })
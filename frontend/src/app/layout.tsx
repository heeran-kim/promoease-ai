import "@/app/globals.css";
import Link from "next/link";

export default function Layout({ children }: { children: React.ReactNode }) {
    return (
        <html lang="en">
            <head>
                <title>PromoEase</title>
                <meta name="description" content="AI-powered social media content management" />
            </head>
            <body className="flex flex-col min-h-screen">
                {/* Navbar */}
                <nav className="bg-blue-500 text-white p-4 flex justify-between">
                    <h1 className="text-xl font-bold">PromoEase</h1>
                    <div className="space-x-4">
                        <Link href="/" className="hover:underline">Home</Link>
                        <Link href="/dashboard" className="hover:underline">Dashboard</Link>
                    </div>
                </nav>

                {/* Main Content */}
                <main className="flex-grow p-4">{children}</main>

                {/* Footer */}
                <footer className="text-center text-gray-500 py-4">
                    © 2025 PromoEase. All rights reserved.
                </footer>
            </body>
        </html>
    );
}
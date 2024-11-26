"use client";

import { AppSidebar } from "@/components/app-sidebar";
import { BrainCog, Sun } from "lucide-react";
import { Button } from "@/components/ui/button";
import {
    Breadcrumb,
    BreadcrumbItem,
    BreadcrumbLink,
    BreadcrumbList,
    BreadcrumbPage,
    BreadcrumbSeparator,
} from "@/components/ui/breadcrumb";

import { Github } from "lucide-react";

import { Separator } from "@/components/ui/separator";

import {
    SidebarInset,
    SidebarProvider,
    SidebarTrigger,
} from "@/components/ui/sidebar";

import { MemoryPieChart } from "@/components/MemoryPieChart";
import { MemoryUsage } from "@/components/MemoryUsage";
import { usePathname } from "next/navigation";

export default function Page() {
    const pathName = usePathname();
    console.log(pathName);
    return (
        <SidebarProvider>
            <AppSidebar />
            <SidebarInset>
                <header className="flex h-16 shrink-0 items-center gap-2 border-b justify-between">
                    <div className="flex items-center gap-2 px-3">
                        <SidebarTrigger />
                        <Separator
                            orientation="vertical"
                            className="mr-2 h-4"
                        />
                        <Breadcrumb>
                            <BreadcrumbList>
                                <BreadcrumbItem className="hidden md:block">
                                    <BreadcrumbLink href="#">
                                        Parent Directory
                                    </BreadcrumbLink>
                                </BreadcrumbItem>
                                <BreadcrumbSeparator className="hidden md:block" />
                                <BreadcrumbItem>
                                    <BreadcrumbPage>
                                        Child Directory
                                    </BreadcrumbPage>
                                </BreadcrumbItem>
                            </BreadcrumbList>
                        </Breadcrumb>
                    </div>
                    <div className="flex gap-2 px-5">
                        <Button variant={"outline"}>
                            <Github />
                        </Button>
                        <Button variant={"outline"}>
                            <Sun />
                        </Button>
                    </div>
                </header>
                <div className="grid grid-rows-2 gap-4 p-4 h-full">
                    <div className="grid md:grid-cols-5 gap-4">
                        <div className="col-span-2 h-full">
                            <MemoryPieChart />
                        </div>
                        <div className="col-span-3 h-full">
                            <MemoryPieChart />
                        </div>
                    </div>
                    <div className="grid auto-rows-min gap-4 md:grid-cols-3">
                        <MemoryPieChart />
                        <div className="col-span-2">
                            <MemoryPieChart />
                        </div>
                    </div>
                </div>
            </SidebarInset>
        </SidebarProvider>
    );
}

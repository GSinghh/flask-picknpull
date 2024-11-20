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

import { CPUPieChart } from "@/components/CPUPieChart";
import { MemoryUsage } from "@/components/MemoryUsage";

export default function Page() {
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
                <div className="flex flex-1 flex-col gap-4 p-4">
                    <div className="grid auto-rows-min gap-4 md:grid-cols-3">
                        <div className="col-span-2">
                            <CPUPieChart />
                        </div>
                        <MemoryUsage />
                    </div>
                    <div className="grid auto-rows-min gap-4 md:grid-cols-3">
                        <CPUPieChart />
                        <div className="col-span-2">
                            <CPUPieChart />
                        </div>
                    </div>
                </div>
            </SidebarInset>
        </SidebarProvider>
    );
}

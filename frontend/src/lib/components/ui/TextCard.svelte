<script lang="ts">
    import { Eye, BookOpen, TrendingUp } from "@lucide/svelte";
	import { Button, Progress, StatCard } from ".";
	import { goto } from "$app/navigation";

    export interface TextType {
        id: number
        title: string
        author: string
        language: string
        totalWords: number
        totalKnowWords: number 
        img_path?: string
    }

    interface TextCardProps {
        text: TextType
        onDetail: (textId: number) => void
    }

    let { text, onDetail }: TextCardProps = $props();
    text.img_path ??= '/default_book.png';

    let percentage = $derived.by(() => {
        return text.totalWords > 0 ? Math.round((text.totalKnowWords / text.totalWords)  * 100) : 0
    });

</script>


<div class="card">
    <div class="img">
        <div>
            <img src={text.img_path} alt="">
        </div>
    </div>
    <div class="content">
        <div class="top">
            <h2>{text.title}</h2>
            <p>{text.author}</p>
            <p>{text.language}</p>
        </div>
        <div class="middle">
            <Progress
                current={text.totalKnowWords}
                total={text.totalWords}
            />

            <StatCard
            statCard={{
                icon:BookOpen,
                primary:String(text.totalKnowWords),
                secondary:`de ${text.totalWords} palavras`
            }} 
            />

            <StatCard
                statCard={{
                    icon:TrendingUp,
                    primary:`${percentage}%`,
                    secondary:"vocabulário"
                }}
            />
           
        </div>
        <div class="buttons">
            <Button
                size='small'
                onclick={() => goto(`/texts/${text.id}`)}
            >
                <BookOpen />
                Continuar leitura
            </Button>
            <Button
                size='small'
                variant='outline'
                onclick={() => onDetail(text.id)}
            >
                <Eye/>
                Detalhes
            </Button>
        </div>
    </div>
</div>

<style>
    .card {
        padding: 1rem 2rem;
        background: var(--background-white);
        border:1px solid var(--border);
        border-radius: 8px;
        display: flex;
        gap: 1rem;
        
    }

    .content {
        display: flex;
        flex-direction: column;
        gap: 0.5rem;
        flex: 1;
    }

    .middle {
        display: flex;
        justify-content: space-between;
    }

    img {
        height: 100px;
        width: 80px;
        object-fit: cover;
        border-radius: 8px;
    }

    .buttons {
        display: flex;
        gap: 1rem;
    }
</style>
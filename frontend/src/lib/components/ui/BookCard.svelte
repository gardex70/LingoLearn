<script lang="ts">
    import { Eye, BookOpen, TrendingUp } from "@lucide/svelte";
	import { Button, Progress, StatCard } from ".";
	import { goto } from "$app/navigation";


    interface BookCardType {
        id: number
        title: string
        autor: string
        img_path?: string
        language: string
        know_words: number
        total_unique_words: number 
    }

    interface BookCardProps {
        bookCard: BookCardType
    }

    let { bookCard }: BookCardProps = $props();

    bookCard.img_path ??= '/default_book.png';

    let percentage = $derived.by(() => {
        return bookCard.total_unique_words > 0 ? Math.round((bookCard.know_words / bookCard.total_unique_words)  * 100) : 0
    });

</script>


<div class="card">
    <div class="img">
        <div>
            <img src={bookCard.img_path} alt="">
        </div>
    </div>
    <div class="content">
        <div class="top">
            <h2>{bookCard.title}</h2>
            <p>{bookCard.autor}</p>
            <p>{bookCard.language}</p>
        </div>
        <div class="middle">
            <Progress
                current={10}
                total={20}
            />

            <StatCard
            statCard={{
                icon:BookOpen,
                primary:String(bookCard.know_words),
                secondary:`de ${bookCard.total_unique_words} palavras`
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
                onclick={() => goto(`/texts/${bookCard.id}`)}
            >
                <BookOpen />
                Continuar leitura
            </Button>
            <Button
                size='small'
                variant='outline'
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
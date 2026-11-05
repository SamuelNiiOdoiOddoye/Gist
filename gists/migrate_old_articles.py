
from django.db import connection, transaction


@transaction.atomic
def migrate_articles():
    with connection.cursor() as cursor:

        # Safety checks: ensure we are migrating the expected data.
        cursor.execute("SELECT COUNT(*) FROM articles_article")
        old_count = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM gists_gist")
        gist_count = cursor.fetchone()[0]

        if old_count != 3 or gist_count != 5:
            raise Exception(
                f"Unexpected database state: "
                f"{old_count} old articles, {gist_count} existing gists. "
                "Migration cancelled."
            )

        # Ensure existing Gist engagement is not overwritten.
        for table in [
            "gists_gist_likes",
            "gists_gist_dislikes",
            "gists_gist_reposts",
        ]:
            cursor.execute(f'SELECT COUNT(*) FROM "{table}"')
            if cursor.fetchone()[0] != 0:
                raise Exception(
                    f"{table} is not empty. Migration cancelled."
                )

        # Read the original Articles.
        cursor.execute("""
            SELECT id, title, body, date_posted, updated_at, author_id
            FROM articles_article
            ORDER BY id
        """)

        articles = cursor.fetchall()

        # Old article ID -> newly generated Gist ID.
        id_mapping = {}

        for article in articles:
            old_id, title, body, date_posted, updated_at, author_id = article

            cursor.execute("""
                INSERT INTO gists_gist
                (title, body, date_posted, updated_at, author_id)
                VALUES (%s, %s, %s, %s, %s)
            """, [title, body, date_posted, updated_at, author_id])

            new_id = cursor.lastrowid
            id_mapping[old_id] = new_id

            # Transfer likes, dislikes and reposts.
            for old_table, new_table in [
                ("articles_article_likes", "gists_gist_likes"),
                ("articles_article_dislikes", "gists_gist_dislikes"),
                ("articles_article_reposts", "gists_gist_reposts"),
            ]:
                cursor.execute(f"""
                    INSERT INTO {new_table} (gist_id, customuser_id)
                    SELECT %s, customuser_id
                    FROM {old_table}
                    WHERE article_id = %s
                """, [new_id, old_id])

        # Verify the resulting counts.
        cursor.execute("SELECT COUNT(*) FROM gists_gist")
        final_count = cursor.fetchone()[0]

        if final_count != 8:
            raise Exception(
                f"Expected 8 Gists, found {final_count}. Rolling back."
            )

        print("\nMigration successful!")
        print("Old Article ID -> New Gist ID:")

        for old_id, new_id in id_mapping.items():
            print(f"{old_id} -> {new_id}")

        print(f"\nTotal Gists: {final_count}")

        for table in [
            "gists_gist_likes",
            "gists_gist_dislikes",
            "gists_gist_reposts",
        ]:
            cursor.execute(f'SELECT COUNT(*) FROM "{table}"')
            print(f"{table}: {cursor.fetchone()[0]}")


migrate_articles()

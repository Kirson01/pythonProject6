"""followers

Revision ID: b155d8ccb541
Revises: a864d571ad0a
Create Date: 2024-06-12 14:18:27.636870

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b155d8ccb541'
down_revision = 'a864d571ad0a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.add_column(sa.Column('body', sa.String(length=140), nullable=True))
        batch_op.drop_column('post')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.add_column(sa.Column('post', sa.VARCHAR(length=140), nullable=True))
        batch_op.drop_column('body')

    op.drop_table('followers')
    # ### end Alembic commands ###
